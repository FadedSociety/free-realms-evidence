# evidence_sync.ps1: mirror the curated evidence into the private GitHub repo FadedSociety/free-realms-evidence
# and push it (lead, 2026-10-24; Bryce: "Private github for evidence"). lab/ is never committed to the game repo,
# so this is the only off-machine copy. The repo is PRIVATE: it holds copyrighted wiki, article and forum text.
#   powershell -NoProfile -ExecutionPolicy Bypass -File lab\fleet\evidence_sync.ps1 [-Message "..."]
param([string]$Message = "")
$ErrorActionPreference = "Stop"
$lab = "C:\Users\Bryce\Documents\Projects\CartoonMMO\lab"
$repo = "C:\Users\Bryce\Documents\Projects\CartoonMMO-evidence"
# source (under lab) -> destination (under the repo); every folder is mirrored, so deletions carry over.
$mirrors = @(
    @("references\quest-lines", "references\quest-lines"),
    @("references\articles", "references\articles"),
    @("references\freerealms-com", "references\freerealms-com"),
    @("references\freerealmsforums", "references\freerealmsforums"),
    @("references\freerealms-wiki\harvest\lists", "references\freerealms-wiki\harvest\lists"),
    @("fleet\out", "fleet\out"),
    @("fleet\jobs", "fleet\jobs"),
    @("fleet\quests", "fleet\quests"),
    @("reports\pin-audit-20261024", "reports\pin-audit-20261024")
)
foreach ($m in $mirrors) {
    $src = Join-Path $lab $m[0]; $dst = Join-Path $repo $m[1]
    if (-not (Test-Path $src)) { continue }
    # /MAX keeps every file under GitHub's 100 MB limit; skipped files are listed below.
    robocopy $src $dst /MIR /MT:16 /R:1 /W:1 /MAX:95000000 /XD __pycache__ /XF *.lock *.tmp /NFL /NDL /NJH /NJS /NP | Out-Null
    if ($LASTEXITCODE -ge 8) { throw "robocopy failed for $($m[0]) (exit $LASTEXITCODE)" }
    Get-ChildItem $src -Recurse -File | Where-Object { $_.Length -gt 95000000 } |
        ForEach-Object { Write-Output "skipped (over 95 MB): $($_.FullName)" }
}
# Single files: the harvest README and the fleet's own scripts.
Copy-Item (Join-Path $lab "references\freerealms-wiki\harvest\README.md") (Join-Path $repo "references\freerealms-wiki\harvest\README.md") -Force
New-Item -ItemType Directory -Force (Join-Path $repo "fleet") | Out-Null
Get-ChildItem (Join-Path $lab "fleet") -File -Include *.py, *.md, *.ps1 -Name | ForEach-Object {
    Copy-Item (Join-Path $lab "fleet\$_") (Join-Path $repo "fleet\$_") -Force
}
Set-Location $repo
git add -A
git diff --cached --quiet
if ($LASTEXITCODE -eq 0) { Write-Output "evidence: nothing changed"; exit 0 }
$stamp = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mmZ")
if (-not $Message) { $Message = "Evidence sync $stamp" }
git commit -q -m $Message -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
git push -q origin main
Write-Output "evidence: pushed $(git rev-parse --short HEAD) ($stamp)"
