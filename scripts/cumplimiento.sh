#!/usr/bin/env bash
# Controles de cumplimiento del repositorio (capítulo 27).
# Uso: bash scripts/cumplimiento.sh   → código 0 si los 6 controles pasan.
cd "$(dirname "$0")/.." || exit 1
ok=0; total=0
control() {  # control "descripción" comando...
  total=$((total + 1))
  local desc="$1"; shift
  if "$@" >/dev/null 2>&1; then echo "✔ C$total $desc"; ok=$((ok + 1)); else echo "✘ C$total $desc"; fi
}
control "Licencia MIT presente"                         grep -q "MIT License" LICENSE
control "Gobernanza: SECURITY.md, CODEOWNERS y plantilla de PR" test -f SECURITY.md -a -f .github/CODEOWNERS -a -f .github/pull_request_template.md
control ".env ignorado y fuera del índice"              bash -c 'git check-ignore -q .env && ! git ls-files --error-unmatch .env'
control "Historial sin secretos"                        bash scripts/escaneo_secretos.sh
control "Pruebas unitarias en verde"                    python3 -m unittest discover -s tests
control "Humo: JSON publicado = CSV"                    python3 scripts/humo.py
echo "Cumplimiento: $ok/$total controles"
[ "$ok" -eq "$total" ]
