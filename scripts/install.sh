#!/usr/bin/env sh
set -eu

SKILL_NAME="bigpicture"
TARGET="both"
REPO="${REPO:-ref42/big-picture-skill}"
REF="${REF:-master}"
INSTALL_ROOT=""
FORCE=0

usage() {
  cat <<EOF
Usage: install.sh [codex|claude|both] [options]

Options:
  --target codex|claude|both  Install target. Defaults to both.
  --repo owner/repo           GitHub repository. Defaults to $REPO.
  --ref ref                   Git ref or branch. Defaults to $REF.
  --install-root path         Custom skills root for one target.
  --force, -f                 Replace an existing installed skill.
  --help, -h                  Show this help.
EOF
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    codex|claude|both)
      TARGET="$1"
      ;;
    --target)
      shift
      TARGET="${1:-}"
      ;;
    --repo)
      shift
      REPO="${1:-}"
      ;;
    --ref)
      shift
      REF="${1:-}"
      ;;
    --install-root)
      shift
      INSTALL_ROOT="${1:-}"
      ;;
    --force|-f)
      FORCE=1
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
  shift
done

case "$TARGET" in
  codex|claude|both) ;;
  *)
    echo "Invalid target: $TARGET" >&2
    exit 1
    ;;
esac

if [ -n "$INSTALL_ROOT" ] && [ "$TARGET" = "both" ]; then
  echo "--install-root can only be used with target codex or claude." >&2
  exit 1
fi

if [ -z "${HOME:-}" ]; then
  echo "HOME is not set; pass --install-root explicitly." >&2
  exit 1
fi

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" 2>/dev/null && pwd || pwd)
local_source="$script_dir/../$SKILL_NAME"
local_script="$script_dir/install.sh"
temp_root=""

cleanup() {
  if [ -n "$temp_root" ] && [ -d "$temp_root" ]; then
    rm -rf "$temp_root"
  fi
}
trap cleanup EXIT HUP INT TERM

download_skill() {
  temp_root=$(mktemp -d "${TMPDIR:-/tmp}/big-picture-skill.XXXXXX")
  archive="$temp_root/source.tar.gz"
  url="https://github.com/$REPO/archive/refs/heads/$REF.tar.gz"

  if command -v curl >/dev/null 2>&1; then
    curl -fsSL "$url" -o "$archive"
  elif command -v wget >/dev/null 2>&1; then
    wget -qO "$archive" "$url"
  else
    echo "curl or wget is required to download $REPO." >&2
    exit 1
  fi

  tar -xzf "$archive" -C "$temp_root"
  found=$(find "$temp_root" -type f -path "*/$SKILL_NAME/SKILL.md" -print | head -n 1)

  if [ -z "$found" ]; then
    echo "Downloaded archive did not contain $SKILL_NAME/SKILL.md." >&2
    exit 1
  fi

  dirname "$found"
}

install_one() {
  root="$1"
  name="$2"
  destination="$root/$SKILL_NAME"

  if [ -e "$destination" ]; then
    if [ "$FORCE" -ne 1 ]; then
      echo "$SKILL_NAME already exists at $destination. Re-run with --force to replace it." >&2
      exit 1
    fi
    rm -rf "$destination"
  fi

  mkdir -p "$root"
  cp -R "$source" "$root/"
  echo "Installed $SKILL_NAME for $name at $destination"
}

if [ -f "$local_script" ] && [ -f "$local_source/SKILL.md" ]; then
  source="$local_source"
else
  source=$(download_skill)
fi

if [ -n "$INSTALL_ROOT" ]; then
  install_one "$INSTALL_ROOT" "$TARGET"
else
  if [ "$TARGET" = "codex" ] || [ "$TARGET" = "both" ]; then
    install_one "$HOME/.agents/skills" "codex"
  fi

  if [ "$TARGET" = "claude" ] || [ "$TARGET" = "both" ]; then
    install_one "$HOME/.claude/skills" "claude"
  fi
fi

echo "Restart Codex or Claude Code to load newly installed skills."
