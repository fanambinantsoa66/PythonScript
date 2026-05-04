import mysql.connector

try:
    # 1. Connexion à la base de données
    conn = mysql.connector.connect(
        host="localhost",
        user="fanamby",
        password="ton_pass",
        database="ma_gestion_adherents"
    )

    if conn.is_connected():
        print("✅ Connexion réussie à MariaDB !")
        cursor = conn.cursor()

        # 2. Exécution d'une requête
        cursor.execute("SELECT nom, prenom FROM membres;")

        # 3. Récupération et affichage des données
        lignes = cursor.fetchall()
        print("\n--- Liste des membres ---")
        for ligne in lignes:
            print(f"Nom : {ligne[0]} | Prénom : {ligne[1]}")

except mysql.connector.Error as e:
    print(f"❌ Erreur lors de la connexion : {e}")

finally:
    # 4. Toujours fermer la connexion
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("\n🔒 Connexion fermée.")

