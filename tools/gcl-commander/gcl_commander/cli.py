"""Explicit local execution path; identical governed tool boundaries."""
import argparse
import json
import os
import sys
from .core import Boundary, assert_identity, reconcile, receipt


def main():
    p = argparse.ArgumentParser(description="GCL Commander (CHAD)")
    commands = p.add_subparsers(dest="cmd", required=True)
    commands.add_parser("doctor")
    commands.add_parser("audit")
    commands.add_parser("views")
    r = commands.add_parser("reconcile")
    r.add_argument("--expected-total", type=int, required=True)
    r.add_argument("--apply", action="store_true")
    head = commands.add_parser("repo-head")
    head.add_argument("repo")
    read = commands.add_parser("repo-file")
    read.add_argument("repo")
    read.add_argument("path")
    read.add_argument("--expected-head", required=True)
    pr = commands.add_parser("repo-pr")
    pr.add_argument("repo")
    pr.add_argument("number", type=int)
    commands.add_parser("serve")
    args = p.parse_args()
    try:
        if args.cmd == "serve":
            from .server import main as server_main
            server_main()
            return
        if args.cmd == "doctor":
            output = assert_identity()
        elif args.cmd == "audit":
            output = reconcile(apply=False)
        elif args.cmd == "views":
            from .queue_views import view_audit
            output = view_audit()
        elif args.cmd == "repo-head":
            from .repositories import repository_head
            output = repository_head(args.repo)
        elif args.cmd == "repo-file":
            from .repositories import repository_read_file
            output = repository_read_file(args.repo, args.path, args.expected_head)
        elif args.cmd == "repo-pr":
            from .repositories import repository_pull_request
            output = repository_pull_request(args.repo, args.number)
        elif args.cmd == "reconcile":
            if args.apply and os.environ.get("GCL_COMMANDER_PROJECT_WRITE") != "enabled":
                raise Boundary("PROJECT_WRITE_NOT_ENABLED_IN_LOCAL_SERVICE_CONFIG")
            output = reconcile(apply=args.apply, expected_total=args.expected_total)
        else:
            raise Boundary("UNKNOWN_LOCAL_COMMAND")
        if not isinstance(output, dict):
            raise Boundary("COMMAND_RESULT_INVALID")
        if "receipt" not in output:
            output["receipt"] = receipt(output)
        print(json.dumps(output, indent=2, sort_keys=True))
    except (Boundary, ValueError, KeyError) as exc:
        print("BLOCKED: " + str(exc), file=sys.stderr)
        raise SystemExit(2)

if __name__ == "__main__":
    main()
