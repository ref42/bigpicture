# Contributing

Thanks for improving this skill.

## Local Checks

Run these before opening a pull request:

```sh
python scripts/validate_skill.py big-picture-thinking
bash -n scripts/install.sh
```

If PowerShell is available:

```powershell
$null = [scriptblock]::Create((Get-Content -Raw scripts\install.ps1))
```

## Skill Guidelines

- Keep `big-picture-thinking/SKILL.md` concise and procedural.
- Put detailed optional material in `big-picture-thinking/references/`.
- Do not put user-facing install docs inside the skill folder.
- Keep the skill compatible with both Claude Code and Codex.
- Update `README.md` if install behavior changes.

## Pull Requests

Please include:

- What changed
- Why the change is useful
- Which validation commands you ran
