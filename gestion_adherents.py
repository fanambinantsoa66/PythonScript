#!/usr/bin/env python3
import json
import os
from datetime import datetime

FICHIER = "adherents_maths.json"

def charger_donnees():
    if os.path.exists(FICHIER):
        with open(FICHIER, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"etudiants": []}

def sauvegarder_donnees(data):
    with open(FICHIER, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def ajouter_etudiant():
    print("\n" + "-"*15 + " NOUVEL ADHÉRENT " + "-"*15)
    data = charger_donnees()
    
    # 1. Vérification immédiate du numéro pour éviter les doublons
    numero = input("Numéro étudiant : ").strip()
    if not numero:
        print("❌ Erreur : Le numéro étudiant est obligatoire.")
        return

    if any(e['numero'] == numero for e in data['etudiants']):
        print(f"❌ Erreur : Le numéro {numero} appartient déjà à un adhérent.")
        return

    # 2. Collecte des autres informations
    etudiant = {"numero": numero}
    etudiant["nom"] = input("Nom : ").strip().upper()
    etudiant["prenom"] = input("Prénom : ").strip().title()
    etudiant["niveau"] = input("Niveau (L1/L2/L3/M1/M2/...) : ").strip().upper()
    etudiant["parcours"] = input("Parcours : ").strip()
    etudiant["date_adhesion"] = datetime.now().strftime("%d/%m/%Y")
    etudiant["tel"] = input("Téléphone (facultatif) : ").strip() or "-"
    etudiant["email"] = input("Email (facultatif) : ").strip() or "-"

    # 3. Sauvegarde
    data["etudiants"].append(etudiant)
    sauvegarder_donnees(data)
    print(f"\n✅ {etudiant['prenom']} {etudiant['nom']} a été ajouté avec succès !")

def afficher_liste():
    data = charger_donnees()
    etudiants = data.get("etudiants", [])
    
    if not etudiants:
        print("\nLa liste est vide.")
        return
    
    print(f"\nLISTE DES ADHÉRENTS ({len(etudiants)})")
    print("="*85)
    print(f"{'N°':<4} {'ID':<10} {'NOM':<15} {'PRÉNOM':<15} {'NIVEAU':<10} {'DATE':<12}")
    print("-" * 85)
    
    for i, e in enumerate(etudiants, 1):
        print(f"{i:<4} {e['numero']:<10} {e['nom']:<15} {e['prenom']:<15} {e['niveau']:<10} {e['date_adhesion']}")
    print("="*85)

def rechercher():
    mot = input("\nRechercher (nom, prénom ou numéro) : ").strip().lower()
    if not mot: return

    data = charger_donnees()
    resultats = [
        e for e in data.get("etudiants", [])
        if mot in e["nom"].lower() or mot in e["prenom"].lower() or mot in e["numero"]
    ]
    
    if not resultats:
        print("Aucun résultat trouvé.")
    else:
        print(f"\n{len(resultats)} résultat(s) trouvé(s) :")
        for e in resultats:
            print(f"[{e['numero']}] {e['prenom']} {e['nom']} - {e['niveau']} ({e['parcours']})")

def menu():
    while True:
        # Optionnel : décommente la ligne suivante pour nettoyer l'écran à chaque menu
        # os.system('clear') 
        
        print("\n" + "="*40)
        print("   GESTION ADHÉRENTS – PARCOURS MATHS   ")
        print("="*40)
        print("1. Ajouter un adhérent")
        print("2. Voir la liste complète")
        print("3. Rechercher un étudiant")
        print("4. Quitter")
        print("="*40)
        
        choix = input("Votre choix (1-4) → ").strip()
        
        if choix == "1":
            ajouter_etudiant()
        elif choix == "2":
            afficher_liste()
        elif choix == "3":
            rechercher()
        elif choix == "4":
            print("\nArrêt du programme. Au revoir !\n")
            break
        else:
            print("Choix invalide, réessayez.")

if __name__ == "__main__":
    menu()

