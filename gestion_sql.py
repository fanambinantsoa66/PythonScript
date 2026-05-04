import mysql.connector
from datetime import datetime
import os

# --- CONFIGURATION CONNEXION ---
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="fanamby",
        password="ton_pass", # Remplace par ton mot de passe
        database="ma_gestion_adherents"
    )

def ajouter_etudiant():
    print("\n" + "-"*15 + " NOUVEL ADHÉRENT " + "-"*15)
    
    numero = input("Numéro étudiant : ").strip()
    nom = input("Nom : ").strip().upper()
    prenom = input("Prénom : ").strip().title()
    email = input("Email : ").strip() or "-"
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Requête SQL pour insérer les données
        sql = "INSERT INTO membres (nom, prenom, email, date_inscription) VALUES (%s, %s, %s, %s)"
        valeurs = (nom, prenom, email, datetime.now().date())
        
        cursor.execute(sql, valeurs)
        conn.commit()
        print(f"\n✅ {prenom} {nom} ajouté avec succès dans la base !")
        
    except mysql.connector.Error as err:
        print(f"❌ Erreur Database : {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def afficher_liste():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, nom, prenom, email, date_inscription FROM membres")
        etudiants = cursor.fetchall()
        
        if not etudiants:
            print("\nLa base de données est vide.")
            return
        
        print(f"\nLISTE DES ADHÉRENTS ({len(etudiants)})")
        print("="*85)
        print(f"{'ID':<4} {'NOM':<20} {'PRÉNOM':<20} {'EMAIL':<25} {'DATE':<12}")
        print("-" * 85)
        
        for e in etudiants:
            # e[0]=id, e[1]=nom, e[2]=prenom, e[3]=email, e[4]=date
            print(f"{e[0]:<4} {e[1]:<20} {e[2]:<20} {e[3]:<25} {e[4]}")
        print("="*85)
        
    except mysql.connector.Error as err:
        print(f"❌ Erreur : {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def rechercher():
    mot = input("\nRechercher par nom : ").strip().upper()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Utilisation de LIKE pour une recherche flexible
        sql = "SELECT nom, prenom FROM membres WHERE nom LIKE %s"
        cursor.execute(sql, (f"%{mot}%",))
        
        resultats = cursor.fetchall()
        if not resultats:
            print("Aucun résultat trouvé.")
        else:
            for r in resultats:
                print(f"-> {r[1]} {r[0]}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def menu():
    while True:
        print("\n" + "="*40)
        print("   GESTION ADHÉRENTS (VERSION SQL)   ")
        print("="*40)
        print("1. Ajouter un adhérent")
        print("2. Voir la liste complète")
        print("3. Rechercher un étudiant")
        print("4. Quitter")
        print("="*40)
        
        choix = input("Votre choix (1-4) → ").strip()
        
        if choix == "1": ajouter_etudiant()
        elif choix == "2": afficher_liste()
        elif choix == "3": rechercher()
        elif choix == "4": break

if __name__ == "__main__":
    menu()

