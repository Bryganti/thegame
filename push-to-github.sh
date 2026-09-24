#!/usr/bin/env bash
# Vérkő — első feltöltés GitHubra.
# Használat:
#   1) Hozz létre egy ÜRES repót a GitHubon (NE generálj README-t, .gitignore-t).
#   2) Cseréld ki az alábbi URL-t a sajátodra, majd futtasd:  bash push-to-github.sh
set -e
REMOTE="${1:?Add meg a repó URL-jét, pl: bash push-to-github.sh git@github.com:user/verko.git}"

git init
git add -A
git commit -m "Vérkő — koncepció, 4 régió, 88 küldetés, koncepció-art, zöld filter shader"
git branch -M main
git remote add origin "$REMOTE" 2>/dev/null || git remote set-url origin "$REMOTE"
git push -u origin main
echo "Kész. A repó: $REMOTE"
