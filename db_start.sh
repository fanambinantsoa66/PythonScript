#!/bin/bash
# ======================================

echo "🚀 Démarrage du service MariaDB..."

# Utilisation de 'service' comme tu l'as demandé
sudo service mariadb start

# Vérification du statut
if [ $? -eq 0 ]; then
    echo "✅ MariaDB a été démarré avec succès !"
    echo "   Statut actuel :"
    sudo service mariadb status | head -n 5
else
    echo "❌ Erreur lors du démarrage de MariaDB."
fi
