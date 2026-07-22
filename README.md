<div align="center">
  <img src="assets/logo.svg" alt="Big Picture" width="96"/>
  <h1>Big Picture</h1>
  <p>Zoom out. Understand what's really happening. Act on what matters.</p>
</div>

<br/>

**Big Picture** is an AI agent skill that turns messy, ambiguous problems into a clear map — what's really happening, why it's happening, what matters most, and what to do next.

It works with **Claude Code** and **Codex** out of the box.

---

## Install

**macOS / Linux**

```sh
curl -fsSL https://raw.githubusercontent.com/ref42/bigpicture/master/scripts/install.sh | sh -s -- both
```

**Windows PowerShell**

```powershell
& ([scriptblock]::Create((Invoke-RestMethod https://raw.githubusercontent.com/ref42/bigpicture/master/scripts/install.ps1))) -Target both
```

Restart Claude Code or Codex after installing. Already installed? Add `--force` / `-Force` to overwrite.

---

## Usage

**Claude Code**

```
/bigpicture our deploy pipeline has been flaky for two weeks and three teams have tried to fix it
```

```
/bigpicture I need to decide between joining a seed-stage startup as employee #5 or staying at my current job
```

```
/bigpicture engagement metrics look fine but churn is quietly climbing and we don't know why
```

**Codex**

```
Use $bigpicture to help me understand what's really going on with our team's execution problems
```

---

## What it does

Given any problem — technical, strategic, interpersonal, or creative — Big Picture:

- Restates the real problem, not just the surface symptom
- Maps the system: actors, incentives, bottlenecks, feedback loops
- Separates causes from constraints from choices
- Surfaces hidden assumptions and second-order effects
- Compares tradeoffs honestly
- Gives 2–4 viable paths forward and a recommended next action

It draws on analytical frameworks from systems thinking, software architecture, distributed systems, decision theory, team dynamics, and more — and picks the ones that actually fit your situation.

---

## Problem types

| | |
|---|---|
| **Diagnostic** | Why is this happening? What's the root cause? |
| **Strategic** | Which direction should we take? |
| **Decision** | Comparing options, feeling stuck choosing |
| **Systems** | Actors, incentives, feedback loops, structural causes |
| **Technical** | Architecture, failure modes, engineering tradeoffs |
| **Product / business** | Market, customers, distribution, positioning |
| **Career / learning** | Goals, opportunity cost, skill leverage |
| **Conflict / org** | Stakeholders, power, trust, communication |
| **Creative / comms** | Audience, message, narrative, framing |

---

## Install options

Install for a single agent:

```sh
# Claude Code only
curl -fsSL https://raw.githubusercontent.com/ref42/bigpicture/master/scripts/install.sh | sh -s -- claude

# Codex only
curl -fsSL https://raw.githubusercontent.com/ref42/bigpicture/master/scripts/install.sh | sh -s -- codex
```

```powershell
# Claude Code only
& ([scriptblock]::Create((Invoke-RestMethod https://raw.githubusercontent.com/ref42/bigpicture/master/scripts/install.ps1))) -Target claude

# Codex only
& ([scriptblock]::Create((Invoke-RestMethod https://raw.githubusercontent.com/ref42/bigpicture/master/scripts/install.ps1))) -Target codex
```

Install from a clone:

```sh
git clone https://github.com/ref42/bigpicture.git
cd bigpicture
sh scripts/install.sh both
```

```powershell
git clone https://github.com/ref42/bigpicture.git
cd bigpicture
.\scripts\install.ps1 -Target both
```

**Install locations**

| Agent | Path |
|---|---|
| Claude Code | `~/.claude/skills/bigpicture` |
| Codex | `~/.agents/skills/bigpicture` |

Use `--install-root` / `-InstallRoot` if your agent reads skills from a custom directory.

---

## Development

Validate the skill:

```sh
python scripts/validate_skill.py bigpicture
bash -n scripts/install.sh
```

Test a local install:

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

---

## License

MIT — see [LICENSE](LICENSE).
