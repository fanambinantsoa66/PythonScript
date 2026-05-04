// personne.cpp
#include "personne.h"
#include <iostream>

using namespace std;

personne::personne() {
    // Constructeur vide
}

void personne::IdentitePerso() {
    cout << "Entrer nom : ";
    cin >> Nom;
    cout << "Entrer prenom : ";
    cin >> Prenom;
    cout << "Votre ID est : " << Nom << " " << Prenom << endl;
}
  
