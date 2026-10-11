"""MCP tool boundary. Local loopback only; expose externally solely via authenticated tunnel."""
from __future__ import annotations
import os
from .core import assert_identity, reconcile, receipt, Boundary
from .repositories import repository_head, repository_read_file, repository_pull_request
from .queue_views import view_audit

try:
    from mcp.server.mcpserver import MCPServer
    _v2 = True
except ImportError:
    from mcp.server.fastmcp import FastMCP as MCPServer
    _v2 = False

mcp = MCPServer("GCL Commander")

@mcp.tool()
def system_status() -> dict:
    """Read-only authenticated GCL operator status; never returns credentials."""
    return {"service": "gcl-commander", "github": assert_identity(),
            "binding": "loopback-only", "operations": ["queue_audit", "queue_view_readback", "governed_repository_read"],
            "project_write_enabled": os.environ.get("GCL_COMMANDER_PROJECT_WRITE")=="enabled",
            "repository_write_enabled": False}

@mcp.tool()
def project_queue_audit() -> dict:
    """Read all GCL Project #2 pages and report semantic queue discrepancies."""
    result = reconcile(apply=False)
    result["receipt"] = receipt(result)
    return result

@mcp.tool()
def project_queue_reconcile(expected_total: int) -> dict:
    """Reconcile semantic queue fields; requires exact inventory count from prior audit.

    Does not change issue labels, status, leases, owner, or return custody.
    GitHub Project mutation requires the configured authenticated operator.
    """
    if os.environ.get("GCL_COMMANDER_PROJECT_WRITE") != "enabled":
        raise Boundary("PROJECT_WRITE_NOT_ENABLED_IN_LOCAL_SERVICE_CONFIG")
    result = reconcile(apply=True, expected_total=expected_total)
    result["receipt"] = receipt(result)
    return result


@mcp.tool()
def project_queue_views_readback() -> dict:
    """Verify exact protected Project #2 EDITORIAL, MATHEMATICS and AVAILABLE saved view IDs and filters."""
    return view_audit()

@mcp.tool()
def governed_repository_head(repo: str) -> dict:
    """Read protected main SHA for one allowlisted GCL repository."""
    return repository_head(repo)

@mcp.tool()
def governed_repository_file(repo: str, path: str, expected_head: str) -> dict:
    """Read a bounded nonsecret source file at the exact protected SHA."""
    return repository_read_file(repo, path, expected_head)

@mcp.tool()
def governed_repository_pr(repo: str, number: int) -> dict:
    """Inspect GitHub PR exact-head, base, author and review evidence, read-only."""
    return repository_pull_request(repo, number)

def main() -> None:
    # Remote ChatGPT must use an authenticated tunnel with the local service;
    # never bind 0.0.0.0 and never expose the raw localhost port.
    if os.environ.get("GCL_COMMANDER_TRANSPORT", "stdio") == "http":
        if _v2:
            mcp.run(transport="streamable-http", host="127.0.0.1",
                    port=int(os.environ.get("GCL_COMMANDER_PORT", "8765")),
                    stateless_http=True, json_response=True)
        else:
            raise Boundary("HTTP_REQUIRES_MCP_V2; install mcp>=2")
    else:
        mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
