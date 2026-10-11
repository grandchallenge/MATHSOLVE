# GCL Commander CHAD: scoped current-user WSL detachment startup installer.
# Requires v0.2.1 source installed at the exact $HOME/gcl-commander root.
# Test detached Linux lifecycle after Windows invocation exits before registration.
# Never reads or logs keys; does not modify GitHub Project or repository state.
$ErrorActionPreference = 'Stop'
$taskName = 'GCL Commander CHAD Tunnel'
$runPath = 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Run'
$runName = 'GCL Commander CHAD Tunnel'
$wsl = Join-Path $env:WINDIR 'System32\wsl.exe'
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$source = Join-Path $scriptDir 'gcl-chad-detached-start.sh'
$logonSource = Join-Path $scriptDir 'start-at-logon.ps1'
$linuxSource = '/home/jim/gcl-commander/deploy/gcl-chad-detached-start.sh'
$linuxDest = '/home/jim/.local/bin/gcl-chad-detached-start.sh'
$expectedSha = '01f4d173613c732fa4203246f47eb1fc645d29d4677144cfd347c36e18df386a'

function Read-Ready {
    $output = & $wsl -d Ubuntu -u jim --exec /usr/bin/curl -s -o /dev/null -w '%{http_code}' --max-time 3 'http://127.0.0.1:8080/readyz' 2>$null
    $result = ("$output").Trim()
    if ($result -match '^[0-9]{3}$') { return $result }
    return '000'
}
function Validate-PS1([string]$path) {
    $tokens = $null
    $parseErrors = $null
    [System.Management.Automation.Language.Parser]::ParseFile($path,[ref]$tokens,[ref]$parseErrors) | Out-Null
    if ($parseErrors.Count -gt 0) {
        foreach ($e in $parseErrors) {
            Write-Host "SYNTAX_ERROR line $($e.Extent.StartLineNumber): $($e.Message)"
        }
        throw 'BLOCKED: invalid logon script syntax'
    }
}

if (!(Test-Path -LiteralPath $source -PathType Leaf) -or !(Test-Path -LiteralPath $logonSource -PathType Leaf)) {
    throw 'BLOCKED: exact packaged startup files missing'
}
if ((Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash.ToLowerInvariant() -ne $expectedSha) {
    throw 'BLOCKED: Linux detached launcher hash mismatch'
}
Validate-PS1 $logonSource
$task = Get-ScheduledTask -TaskName $taskName -ErrorAction Stop
$action = @($task.Actions)
$expectedAction = '-d "Ubuntu" -u "jim" --exec /bin/bash "/home/jim/gcl-commander/deploy/supervise-openai-tunnel-wsl.sh"'
if ($action.Count -ne 1 -or $action[0].Execute -ine $wsl -or $action[0].Arguments -ne $expectedAction) {
    throw 'BLOCKED: protected existing scheduled task identity drift'
}
if ($task.Principal.LogonType -ne 'Interactive') { throw 'BLOCKED: old scheduled task principal drift' }
Write-Host 'TASK_IDENTITY: PASS'
Write-Host "READY_PRE: $(Read-Ready)"

& $wsl -d Ubuntu -u jim --exec /usr/bin/install -m 700 $linuxSource $linuxDest
if ($LASTEXITCODE -ne 0) { throw 'BLOCKED: could not install vetted Linux detached launcher' }
& $wsl -d Ubuntu -u jim --exec /bin/bash -n $linuxDest
if ($LASTEXITCODE -ne 0) { throw 'BLOCKED: Linux detached launcher syntax check failed' }
Write-Host 'LINUX_LAUNCHER_INSTALLED: PASS'

# This is synchronous, unlike the failing Start-Process / scheduled launches.
Write-Host 'TEST: detached Linux supervisor through direct PowerShell-to-WSL invocation'
& $wsl -d Ubuntu -u jim --exec /bin/bash $linuxDest
$launchCode = $LASTEXITCODE
Write-Host "DETACH_LAUNCH_EXIT_CODE: $launchCode"
if ($launchCode -ne 0) { throw 'BLOCKED: detached Linux launch failed; no persistence changes' }

# Deliberately test after the previous wsl.exe process has returned.
Start-Sleep -Seconds 8
$readyOne = Read-Ready
Write-Host "READY_AFTER_WSL_RETURN: $readyOne"
Start-Sleep -Seconds 5
$readyTwo = Read-Ready
Write-Host "READY_AFTER_FURTHER_DELAY: $readyTwo"
& $wsl -d Ubuntu -u jim --exec /usr/bin/pgrep -x tunnel-client *> $null
$processPresent = ($LASTEXITCODE -eq 0)
Write-Host "TUNNEL_CLIENT_PID_EXISTS: $processPresent"
& $wsl -d Ubuntu -u jim --exec /usr/bin/flock -n /home/jim/.local/state/gcl-commander/tunnel-supervisor.lock -c true *> $null
$lockHeld = ($LASTEXITCODE -ne 0)
Write-Host "SUPERVISOR_LOCK_HELD: $lockHeld"
if ($readyOne -ne '200' -or $readyTwo -ne '200' -or !$processPresent -or !$lockHeld) {
    Write-Host 'BLOCKED: Linux supervisor does not survive Windows WSL process exit; no logon registration'
    exit 4
}

# Prepare a stable non-secret Windows user-logon wrapper. Only after live survival.
$directory = Join-Path $env:LOCALAPPDATA 'GCLCommander'
New-Item -Path $directory -ItemType Directory -Force | Out-Null
$installedLogon = Join-Path $directory 'start-at-logon.ps1'
$existingRun = Get-ItemProperty -Path $runPath -Name $runName -ErrorAction SilentlyContinue
$exe = Join-Path $env:WINDIR 'System32\WindowsPowerShell\v1.0\powershell.exe'
$runCommand = '"{0}" -NoProfile -WindowStyle Minimized -ExecutionPolicy Bypass -File "{1}"' -f $exe,$installedLogon
if ($null -ne $existingRun) {
    $existingValue = $existingRun.PSObject.Properties[$runName].Value
    if ($existingValue -ne $runCommand) { throw 'BLOCKED: existing same-name startup Run entry differs; no overwrite' }
}
Copy-Item -LiteralPath $logonSource -Destination $installedLogon -Force
Validate-PS1 $installedLogon
if ((Get-FileHash -LiteralPath $logonSource -Algorithm SHA256).Hash -ne (Get-FileHash -LiteralPath $installedLogon -Algorithm SHA256).Hash) {
    throw 'BLOCKED: installed logon launcher hash mismatch'
}

$createdRun = $false
if ($null -eq $existingRun) {
    New-Item -Path $runPath -Force | Out-Null
    New-ItemProperty -Path $runPath -Name $runName -Value $runCommand -PropertyType String -Force | Out-Null
    $createdRun = $true
}
$readback = (Get-ItemProperty -Path $runPath -Name $runName).PSObject.Properties[$runName].Value
if ($readback -ne $runCommand) {
    if ($createdRun) { Remove-ItemProperty -Path $runPath -Name $runName -ErrorAction SilentlyContinue }
    throw 'BLOCKED: current-user logon Run readback differs'
}
Write-Host 'HKCU_CURRENT_USER_LOGON_STARTUP: REGISTERED_AND_READ_BACK'
try {
    Disable-ScheduledTask -TaskName $taskName -ErrorAction Stop | Out-Null
    Write-Host 'OLD_TASK: disabled but retained for rollback'
} catch {
    if ($createdRun) { Remove-ItemProperty -Path $runPath -Name $runName -ErrorAction SilentlyContinue }
    throw 'BLOCKED: could not disable old conflicting task; new Run entry rolled back when created'
}
$readyFinal = Read-Ready
Write-Host "READY_FINAL_HTTP: $readyFinal"
Write-Host 'RESULT: CURRENT_SESSION_TUNNEL_READY_AND_LOGON_LAUNCH_REGISTERED'
Write-Host 'RESTART_ACCEPTANCE: fresh Windows logon and ChatGPT live MCP tool readback remain required'
Write-Host 'ROLLBACK: delete only the exact GCL Commander HKCU Run entry; re-enable preserved scheduled task'
