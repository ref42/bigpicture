[CmdletBinding()]
param(
    [ValidateSet("codex", "claude", "both")]
    [string]$Target = "both",

    [string]$Repo = "ref42/bigpicture",
    [string]$Ref = "master",
    [string]$InstallRoot,
    [switch]$Force
)

$ErrorActionPreference = "Stop"

$SkillName = "bigpicture"

function Get-HomeDirectory {
    if ($env:HOME) {
        return $env:HOME
    }

    return [Environment]::GetFolderPath("UserProfile")
}

function Get-LocalSkillPath {
    if (-not $PSScriptRoot) {
        return $null
    }

    $candidate = Join-Path $PSScriptRoot "..\big-picture-thinking"
    $skillFile = Join-Path $candidate "SKILL.md"

    if (Test-Path -LiteralPath $skillFile) {
        return (Resolve-Path -LiteralPath $candidate).Path
    }

    return $null
}

function Get-DownloadedSkillPath {
    param(
        [string]$Repo,
        [string]$Ref
    )

    # Ensure TLS 1.2 is available for older PowerShell versions
    try {
        [Net.ServicePointManager]::SecurityProtocol =
            [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12
    } catch {}

    $tempRoot = Join-Path ([IO.Path]::GetTempPath()) ("big-picture-skill-" + [guid]::NewGuid().ToString("N"))
    New-Item -ItemType Directory -Path $tempRoot | Out-Null

    try {
        $archive = Join-Path $tempRoot "source.zip"
        $url = "https://github.com/$Repo/archive/refs/heads/$Ref.zip"

        Invoke-WebRequest -Uri $url -OutFile $archive -UseBasicParsing
        Expand-Archive -LiteralPath $archive -DestinationPath $tempRoot

        $skillDir = Get-ChildItem -LiteralPath $tempRoot -Recurse -File -Filter "SKILL.md" |
            Where-Object { $_.Directory.Name -eq $SkillName } |
            Select-Object -First 1

        if (-not $skillDir) {
            throw "Downloaded archive did not contain $SkillName/SKILL.md."
        }

        return [pscustomobject]@{
            Source = $skillDir.Directory.FullName
            TempRoot = $tempRoot
        }
    }
    catch {
        if (Test-Path -LiteralPath $tempRoot) {
            Remove-Item -LiteralPath $tempRoot -Recurse -Force
        }
        throw
    }
}

function Get-InstallTargets {
    param(
        [string]$Target,
        [string]$InstallRoot
    )

    if ($InstallRoot) {
        if ($Target -eq "both") {
            throw "-InstallRoot can only be used with -Target codex or -Target claude."
        }

        return @([pscustomobject]@{
            Name = $Target
            Root = $InstallRoot
        })
    }

    $userHome = Get-HomeDirectory
    $targets = @()

    if ($Target -eq "codex" -or $Target -eq "both") {
        $targets += [pscustomobject]@{
            Name = "codex"
            Root = Join-Path $userHome ".agents\skills"
        }
    }

    if ($Target -eq "claude" -or $Target -eq "both") {
        $targets += [pscustomobject]@{
            Name = "claude"
            Root = Join-Path $userHome ".claude\skills"
        }
    }

    return $targets
}

function Install-Skill {
    param(
        [string]$Source,
        [string]$Root,
        [string]$Name,
        [bool]$Force
    )

    $destination = Join-Path $Root $SkillName

    if (Test-Path -LiteralPath $destination) {
        if (-not $Force) {
            throw "$SkillName already exists at $destination. Re-run with -Force to replace it."
        }

        Remove-Item -LiteralPath $destination -Recurse -Force
    }

    New-Item -ItemType Directory -Path $Root -Force | Out-Null
    Copy-Item -LiteralPath $Source -Destination $Root -Recurse

    Write-Host "Installed $SkillName for $Name at $destination"
}

$download = $null

try {
    $source = Get-LocalSkillPath

    if (-not $source) {
        $download = Get-DownloadedSkillPath -Repo $Repo -Ref $Ref
        $source = $download.Source
    }

    $targets = Get-InstallTargets -Target $Target -InstallRoot $InstallRoot

    foreach ($targetInfo in $targets) {
        Install-Skill -Source $source -Root $targetInfo.Root -Name $targetInfo.Name -Force:$Force.IsPresent
    }

    Write-Host "Restart Codex or Claude Code to load newly installed skills."
}
finally {
    if ($download -and (Test-Path -LiteralPath $download.TempRoot)) {
        Remove-Item -LiteralPath $download.TempRoot -Recurse -Force
    }
}
