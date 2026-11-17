#!/usr/bin/env bash
# Busca patrones de secretos en TODO el historial antes de cada push.
# Uso: bash scripts/escaneo_secretos.sh   (sale con código 1 si encuentra algo)
patron='ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----|(password|token)=[^ <"]+|@(gmail|hotmail|outlook|yahoo)\.com'
hallazgos=$(git grep -nIE "$patron" $(git rev-list --all) -- ':!scripts/escaneo_secretos.sh' 2>/dev/null)
if [ -n "$hallazgos" ]; then
  echo "$hallazgos"; echo "ALERTA: revisar los hallazgos antes de hacer push"; exit 1
fi
echo "Escaneo de secretos: 0 hallazgos en $(git rev-list --all | wc -l) commits"
