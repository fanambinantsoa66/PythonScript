// personne.h
#ifndef PERSONNE_H
#define PERSONNE_H

#include <iostream>
#include <string>

class personne {
public: // Correction : pas de point-virgule après public
    std::string Nom;
    std::string Prenom;
    
    // Déclarations des méthodes
    void IdentitePerso(); // Doit retourner void si elle ne renvoie rien
    personne();
}; // Ne pas oublier le point-virgule à la fin de la classe

#endif

