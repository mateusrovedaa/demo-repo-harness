#!/usr/bin/env sh
# Gate hook (L4): bloqueia comandos destrutivos antes de executar.
# Recebe o JSON do evento em stdin; responde {"allowed": true|false}.
input=$(cat)
command=$(printf '%s' "$input" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("command",""))' 2>/dev/null)

case "$command" in
  *'rm -rf /'* | *'git push --force'* | *'git push -f'* | *'dd if=/dev/zero'*)
    printf '{"allowed": false, "denyReason": "Comando destrutivo bloqueado pelo harness."}'
    ;;
  *)
    printf '{"allowed": true}'
    ;;
esac