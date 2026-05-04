"""
import time
import os

# Temps d'attente en secondes (ex: 600 pour 10 minutes)
INTERVALLE = 10 

while True:
    time.sleep(INTERVALLE)
    # Affiche le message directement dans le terminal actif
    os.system('echo "\n\033[1;32m[Rappel] : C\'est l\'heure d'apprendre le langage Python pour vous !\033[0m"')

"""
