#!/usr/bin/env python3
import os
import platform
import sys

def check_userland_env():
    print("--- 🛠️ Diagnostic Système UserLand ---")
    
    # Informations sur l'OS
    print(f"OS : {platform.system()} {platform.release()}")
    print(f"Architecture : {platform.machine()}")
    print(f"Version Python : {sys.version.split()[0]}")
    
    print("\n--- 📁 Contenu du dossier actuel ---")
    files = os.listdir('.')
    if not files:
        print("Le dossier est vide.")
    for file in files:
        size = os.path.getsize(file)
        print(f"- {file} ({size} octets)")

    print("\n--- 👤 Utilisateur ---")
    print(f"Utilisateur actuel : {os.getlogin()}")

if __name__ == "__main__":
    check_userland_env()

