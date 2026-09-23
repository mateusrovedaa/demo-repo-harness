#!/usr/bin/env sh
# Feedback hook (L4): formata o arquivo editado com ruff, em tempo real.
# Recebe o JSON do evento em stdin; o campo "file" indica o arquivo alterado.
input=$(cat)
file=$(printf '%s' "$input" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("file",""))' 2>/dev/null)

case "$file" in
  *.py) ruff format "$file" 2>/dev/null ;;
esac
exit 0