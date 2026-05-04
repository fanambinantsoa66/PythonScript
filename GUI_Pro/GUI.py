# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

def connecter_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="fanamby", # Ton utilisateur habituel
            password="ton_pass",
            database="NOM_DE_TA_BASE"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Erreur SQL", f"Impossible de se connecter : {err}")
        return None

# --- 1. FONCTIONS DE NAVIGATION ---
def focus_suivant(event):
    """Déplace le curseur au champ suivant avec la touche Entrée"""
    event.widget.tk_focusNext().focus()
    return "break"

# --- 2. LOGIQUE / FONCTIONS D'ACTION ---

def ajouter_adherent():
    # Récupération des données
    nom = ent_nom.get().strip()
    prenom = ent_prenom.get().strip()
    niveau = combo_niveau.get()
    parcours = ent_parcours.get().strip()
    email = ent_email.get().strip()

    # Vérification des champs obligatoires
    if not nom or not niveau or not parcours or not email:
        messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs obligatoires (*)")
        return

    # Fenêtre de confirmation (OK / Annuler)
    recap = f"Nom: {nom}\nPrenom: {prenom}\nNiveau: {niveau}\nParcours: {parcours}\nEmail: {email}"
    confirmation = messagebox.askokcancel("Confirmation", f"Confirmez-vous l'ajout de :\n\n{recap}")

    if confirmation:
        # TODO: Insertion SQL ici (mysql.connector)
        messagebox.showinfo("Succes", f"Adherent {nom} enregistre avec succes !")
        
        # Réinitialisation
        ent_nom.delete(0, tk.END)
        ent_prenom.delete(0, tk.END)
        combo_niveau.set('')
        ent_parcours.delete(0, tk.END)
        ent_email.delete(0, tk.END)
        ent_nom.focus() # Retour au début

def voir_liste():
    messagebox.showinfo("Base de donnees", "Connexion a MySQL pour afficher la liste...")

def chercher_adherent():
    messagebox.showinfo("Recherche", "Connexion a MySQL pour la recherche...")

def confirmer_quitter():
    reponse = messagebox.askyesno("Confirmation", "Voulez-vous vraiment quitter ?")
    if reponse:
        root.destroy()

# --- 3. INTERFACE GRAPHIQUE ---
root = tk.Tk()
root.title("Gestion Adherents - Fanamby v2.0")
root.geometry("500x600")
root.configure(bg="#e8e8e8")

# Titre
tk.Label(root, text="SYSTEME DE GESTION DES ADHERENTS", font=("Arial", 14, "bold"), bg="#e8e8e8").pack(pady=15)

# --- 4. FORMULAIRE ---
frame_form = tk.LabelFrame(root, text=" Nouveau Membre ", padx=20, pady=20, bg="#e8e8e8")
frame_form.pack(padx=20, pady=10, fill="both")

lbl_style = {"bg": "#e8e8e8", "font": ("Arial", 10)}

# Champs + Liaisons (Binding)
tk.Label(frame_form, text="Nom (*) :", **lbl_style).grid(row=0, column=0, sticky="w")
ent_nom = tk.Entry(frame_form, width=30)
ent_nom.grid(row=0, column=1, pady=5)
ent_nom.bind("<Return>", focus_suivant) # Lie la touche Entrée

tk.Label(frame_form, text="Prenom :", **lbl_style).grid(row=1, column=0, sticky="w")
ent_prenom = tk.Entry(frame_form, width=30)
ent_prenom.grid(row=1, column=1, pady=5)
ent_prenom.bind("<Return>", focus_suivant)

tk.Label(frame_form, text="Niveau (*) :", **lbl_style).grid(row=2, column=0, sticky="w")
combo_niveau = ttk.Combobox(frame_form, values=["L1", "L2", "L3", "M1", "M2"], state="readonly", width=28)
combo_niveau.grid(row=2, column=1, pady=5)
combo_niveau.bind("<Return>", focus_suivant)

tk.Label(frame_form, text="Parcours (*) :", **lbl_style).grid(row=3, column=0, sticky="w")
ent_parcours = tk.Entry(frame_form, width=30)
ent_parcours.grid(row=3, column=1, pady=5)
ent_parcours.bind("<Return>", focus_suivant)

tk.Label(frame_form, text="Email (*) :", **lbl_style).grid(row=4, column=0, sticky="w")
ent_email = tk.Entry(frame_form, width=30)
ent_email.grid(row=4, column=1, pady=5)
# Sur le dernier champ, Entrée peut lancer l'enregistrement :
ent_email.bind("<Return>", lambda e: ajouter_adherent())

# --- 5. BOUTONS D'ACTION ---
btn_style = {"width": 25, "font": ("Arial", 10, "bold"), "fg": "white"}

tk.Button(root, text="Enregistrer", command=ajouter_adherent, bg="#2ecc71", **btn_style).pack(pady=5)
tk.Button(root, text="Voir la Liste", command=voir_liste, bg="#3498db", **btn_style).pack(pady=5)
tk.Button(root, text="Chercher un Membre", command=chercher_adherent, bg="#f1c40f", **btn_style).pack(pady=5)
tk.Button(root, text="❌ QUITTER", command=confirmer_quitter, bg="#e74c3c", **btn_style).pack(pady=20)

if __name__ == "__main__":
    ent_nom.focus() # Met le curseur sur le Nom au démarrage
    root.mainloop()
