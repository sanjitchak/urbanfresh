#!/bin/zsh
set -eu

LABEL="com.urbanfresh.seo-improver"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TEMPLATE="$ROOT/scripts/$LABEL.plist.template"
LAUNCH_AGENTS="$HOME/Library/LaunchAgents"
TARGET="$LAUNCH_AGENTS/$LABEL.plist"

mkdir -p "$LAUNCH_AGENTS"
sed "s|__ROOT__|$ROOT|g" "$TEMPLATE" > "$TARGET"
plutil -lint "$TARGET"
launchctl bootout "gui/$UID" "$TARGET" >/dev/null 2>&1 || true
launchctl bootstrap "gui/$UID" "$TARGET"
launchctl enable "gui/$UID/$LABEL"

echo "Installed $LABEL"
echo "Runs every Monday at 09:00 local time."
echo "Run now: launchctl kickstart -k gui/$UID/$LABEL"
