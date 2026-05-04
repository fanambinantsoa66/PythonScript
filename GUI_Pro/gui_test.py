# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox, ttk

# --- FONCTIONS ---
def ajouter():
    nom = entree_nom.get()
    if nom:
        # Ici on simulera l'ajout (on liera ta BDD plus tard)
        messagebox.showinfo("Succes", f"Adherent {nom} enregistre !")
        entree_nom.delete(0, tk.END)
    else:
        messagebox.showwarning("Attention", "Entrez un nom")

def voir_liste():
    # Fenetre secondaire pour la liste
    messagebox.showinfo("Liste", "Affichage de la liste (Bientot connecte a SQL)")

def recherche():
    messagebox.showinfo("Recherche", "Fonction de recherche en cours...")

# --- INTERFACE PRINCIPALE ---
root = tk.Tk()
root.title("Systeme de Gestion - Fanamby")
root.geometry("450x400")
root.configure(bg="#f0f0f0")

# Titre
tk.Label(root, text="MENU GESTION ADHERENTS", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=15)

# Zone de saisie
tk.Label(root, text="Nom de l'Adherent :", bg="#f0f0f0").pack()
entree_nom = tk.Entry(root, width=35)
entree_nom.pack(pady=5)

# Boutons (Style Pro)
style_btn = {"width": 25, "font": ("Arial", 10)}

tk.Button(root, text=" Ajouter Adherent", command=ajouter, bg="#4CAF50", fg="white", **style_btn).pack(pady=5)
tk.Button(root, text=" Voir la Liste", command=voir_liste, bg="#2196F3", fg="white", **style_btn).pack(pady=5)
tk.Button(root, text=" Rechercher", command=recherche, bg="#FF9800", fg="white", **style_btn).pack(pady=5)
tk.Button(root, text=" Quitter", command=root.quit, bg="#f44336", fg="white", **style_btn).pack(pady=20)

if __name__ == "__main__":
    root.mainloop()

