# GCL Commander: current-user logon shim.
# Synchronous Windows -> WSL; Linux launcher detaches existing supervisor.
# Does not read or store runtime credentials.
$ErrorActionPreference = 'Stop'
$wsl = Join-Path $env:WINDIR 'System32\wsl.exe'
& $wsl -d Ubuntu -u jim --exec /bin/bash /home/jim/.local/bin/gcl-chad-detached-start.sh
$rc = $LASTEXITCODE
if ($rc -ne 0) { exit $rc }
exit 0
