# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox, ttk

# --- LOGIQUE DE L'APPLICATION ---

def ajouter_adherent():
    # Récupération des données
    nom = ent_nom.get().strip()
    prenom = ent_prenom.get().strip()
    niveau = combo_niveau.get()
    parcours = ent_parcours.get().strip()
    email = ent_email.get().strip()

    # Vérification des champs obligatoires (comme dans ton script précédent)
    if not nom or not niveau or not parcours or not email:
        messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs obligatoires (*)")
        return

    # TODO : Ici nous insérerons le code mysql.connector
    # Pour l'instant, on simule le succès
    infos = f"Nom: {nom}\nPrenom: {prenom}\nNiveau: {niveau}\nParcours: {parcours}\nEmail: {email}"
    messagebox.showinfo("Succes", f"Adherent ajoute avec succes !\n\n{infos}")
    
    # Réinitialisation du formulaire
    ent_nom.delete(0, tk.END)
    ent_prenom.delete(0, tk.END)
    ent_parcours.delete(0, tk.END)
    ent_email.delete(0, tk.END)

def voir_liste():
    # TODO : Requete SELECT * FROM adherents
    messagebox.showinfo("Base de donnees", "Connexion a MySQL pour afficher la liste...")

# --- 2. LOGIQUE / FONCTIONS ---

def chercher_adherent():
    # Ton code de recherche actuel...
    messagebox.showinfo("Recherche", "Connexion a MySQL...")

def confirmer_quitter():
    """Fonction pour l'Option 4 : Quitter avec confirmation"""
    reponse = messagebox.askyesno("Confirmation", "Voulez-vous vraiment quitter ?")
    if reponse:
        root.destroy()

# --- INTERFACE GRAPHIQUE ---

root = tk.Tk()
root.title("Gestion Adherents - Fanamby v2.0")
root.geometry("500x550")
root.configure(bg="#e8e8e8")

# Titre principal
tk.Label(root, text="SYSTEME DE GESTION DES ADHERENTS", font=("Arial", 14, "bold"), bg="#e8e8e8", fg="#333").pack(pady=15)

# --- FORMULAIRE ---
frame_form = tk.LabelFrame(root, text=" Nouveau Membre ", padx=20, pady=20, bg="#e8e8e8")
frame_form.pack(padx=20, pady=10, fill="both")

# Configuration des labels et entrées
lbl_style = {"bg": "#e8e8e8", "font": ("Arial", 10)}

# Nom (Obligatoire)
tk.Label(frame_form, text="Nom (*) :", **lbl_style).grid(row=0, column=0, sticky="w")
ent_nom = tk.Entry(frame_form, width=30)
ent_nom.grid(row=0, column=1, pady=5)

# Prénom
tk.Label(frame_form, text="Prenom :", **lbl_style).grid(row=1, column=0, sticky="w")
ent_prenom = tk.Entry(frame_form, width=30)
ent_prenom.grid(row=1, column=1, pady=5)

# Niveau (Obligatoire - Liste déroulante)
tk.Label(frame_form, text="Niveau (*) :", **lbl_style).grid(row=2, column=0, sticky="w")
combo_niveau = ttk.Combobox(frame_form, values=["L1", "L2", "L3", "M1", "M2"], state="readonly", width=28)
combo_niveau.grid(row=2, column=1, pady=5)

# Parcours (Obligatoire)
tk.Label(frame_form, text="Parcours (*) :", **lbl_style).grid(row=3, column=0, sticky="w")
ent_parcours = tk.Entry(frame_form, width=30)
ent_parcours.grid(row=3, column=1, pady=5)

# Email (Obligatoire)
tk.Label(frame_form, text="Email (*) :", **lbl_style).grid(row=4, column=0, sticky="w")
ent_email = tk.Entry(frame_form, width=30)
ent_email.grid(row=4, column=1, pady=5)

# --- BOUTONS D'ACTION ---
btn_style = {"width": 20, "font": ("Arial", 10, "bold"), "fg": "white"}

tk.Button(root, text="Enregistrer", command=ajouter_adherent, bg="#2ecc71", **btn_style).pack(pady=5)
tk.Button(root, text="Voir la Liste", command=voir_liste, bg="#3498db", **btn_style).pack(pady=5)
tk.Button(root, text="Chercher un Membre", command=chercher_adherent, bg="#f1c40f", **btn_style).pack(pady=5)
tk.Button(root, text="Quitter", command=root.quit, bg="#e74c3c", **btn_style).pack(pady=20)

if __name__ == "__main__":
    root.mainloop()
# --- 5. BOUTONS D'ACTION ---
btn_style = {"width": 25, "font": ("Arial", 10, "bold"), "fg": "white"}

# Option 1
tk.Button(root, text="Enregistrer", command=ajouter_adherent, bg="#2ecc71", **btn_style).pack(pady=5)

# Option 2
tk.Button(root, text="Voir la Liste", command=voir_liste, bg="#3498db", **btn_style).pack(pady=5)

# Option 3
tk.Button(root, text="Chercher un Membre", command=chercher_adherent, bg="#f1c40f", **btn_style).pack(pady=5)

# OPTION 4 : QUITTER (Ajoute-le ici)
tk.Button(root, text="❌ QUITTER", command=confirmer_quitter, bg="#e74c3c", **btn_style).pack(pady=20)
