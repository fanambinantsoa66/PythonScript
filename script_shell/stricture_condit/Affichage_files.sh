#!/bin/bash

# =============================================
# Liste tous les scripts shell dans un répertoire
# =============================================

REPERTOIRE="/home/fanamby/script_shell/stricture_condit"

echo "🔍 Recherche des fichiers .sh dans : $REPERTOIRE"
echo "────────────────────────────────────────"

if [ ! -d "$REPERTOIRE" ]; then
    echo "❌ Le répertoire n'existe pas : $REPERTOIRE"
    exit 1
fi

# Utilisation de find (plus robuste)
NB_FICHIERS=$(find "$REPERTOIRE" -maxdepth 1 -name "*.sh" -type f | wc -l)

if [ "$NB_FICHIERS" -eq 0 ]; then
    echo "Aucun fichier .sh trouvé dans le répertoire."
else
    echo "✅ $NB_FICHIERS fichier(s) .sh trouvé(s) :"
    echo
    
    find "$REPERTOIRE" -maxdepth 1 -name "*.sh" -type f -print0 | sort -z | while IFS= read -r -d '' fichier; do
        nom=$(basename "$fichier")
        echo "• $nom"
    done
fi
