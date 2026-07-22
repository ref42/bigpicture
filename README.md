# Big Picture Thinking Skill

An open Agent Skill for zooming out from messy problems into clearer systems, tradeoffs, and next actions.

The same skill folder works with both Claude Code and Codex because it uses the standard `SKILL.md` package layout.

## Install

Install for both Claude Code and Codex:

### macOS / Linux

```sh
curl -fsSL https://raw.githubusercontent.com/ref42/bigpicture/master/scripts/install.sh | sh -s -- both
```

### Windows PowerShell

```powershell
& ([scriptblock]::Create((Invoke-RestMethod https://raw.githubusercontent.com/ref42/bigpicture/master/scripts/install.ps1))) -Target both
```

Install for only one agent:

```sh
curl -fsSL https://raw.githubusercontent.com/ref42/bigpicture/master/scripts/install.sh | sh -s -- claude
curl -fsSL https://raw.githubusercontent.com/ref42/bigpicture/master/scripts/install.sh | sh -s -- codex
```

```powershell
& ([scriptblock]::Create((Invoke-RestMethod https://raw.githubusercontent.com/ref42/bigpicture/master/scripts/install.ps1))) -Target claude
& ([scriptblock]::Create((Invoke-RestMethod https://raw.githubusercontent.com/ref42/bigpicture/master/scripts/install.ps1))) -Target codex
```

If the skill is already installed, add `--force` on macOS/Linux or `-Force` on Windows.

Restart Claude Code or Codex after installing.

## Install From A Clone

```sh
git clone https://github.com/ref42/bigpicture.git
cd big-picture-skill
sh scripts/install.sh both
```

```powershell
git clone https://github.com/ref42/bigpicture.git
cd big-picture-skill
.\scripts\install.ps1 -Target both
```

## Install Locations

The installer copies `bigpicture/` to:

- Claude Code: `~/.claude/skills/bigpicture`
- Codex: `~/.agents/skills/bigpicture`

Use `--install-root` or `-InstallRoot` if your agent is configured to read skills from another directory.
For older Codex setups that still use `~/.codex/skills`, install with:

```sh
curl -fsSL https://raw.githubusercontent.com/ref42/bigpicture/master/scripts/install.sh | sh -s -- codex --install-root "$HOME/.codex/skills"
```

```powershell
& ([scriptblock]::Create((Invoke-RestMethod https://raw.githubusercontent.com/ref42/bigpicture/master/scripts/install.ps1))) -Target codex -InstallRoot "$HOME\.codex\skills"
```

## Usage

Claude Code:

```text
/bigpicture help me understand the bigger picture behind this product decision
```

Codex:

```text
Use $bigpicture to zoom out from this technical debugging problem and identify the real system failure.
```

## What It Helps With

- Understanding the bigger picture behind a confusing problem
- Separating symptoms, causes, constraints, and choices
- Mapping actors, incentives, bottlenecks, and feedback loops
- Comparing options when you feel stuck
- Turning broad strategic analysis into a concrete next action
- Zooming out from technical, product, business, career, organizational, creative, or personal planning problems

## Repository Layout

```text
big-picture-skill/
  bigpicture/
    SKILL.md
    agents/
      openai.yaml
    references/
      lenses.md
      playbooks.md
      question-bank.md
      templates.md
  scripts/
    install.ps1
    install.sh
    validate_skill.py
  .github/
    workflows/
      validate.yml
```

The actual skill is `bigpicture/`. Everything else supports installation, validation, and distribution.

## Development

Validate the skill locally:

```sh
python scripts/validate_skill.py bigpicture
bash -n scripts/install.sh
```

On systems with PowerShell:

```powershell
$null = [scriptblock]::Create((Get-Content -Raw scripts\install.ps1))
```

Test an install into a temporary directory:

```sh
tmp="$(mktemp -d)"
sh scripts/install.sh codex --install-root "$tmp"
test -f "$tmp/bigpicture/SKILL.md"
```

```powershell
$tmp = Join-Path ([IO.Path]::GetTempPath()) ([guid]::NewGuid().ToString("N"))
.\scripts\install.ps1 -Target codex -InstallRoot $tmp
Test-Path (Join-Path $tmp "bigpicture\SKILL.md")
```

## License

MIT License. See [LICENSE](LICENSE).
