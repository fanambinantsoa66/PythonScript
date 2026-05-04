#include "Rectangle.h"
#include <iostream>

using namespace std;

// Implémentation du constructeur
Rectangle::Rectangle(double L, double l) {
    longueur = L;
    largeur = l;
}

// Calcul de la surface
double Rectangle::calculerSurface() {
    return longueur * largeur;
}

// Affichage des détails
void Rectangle::afficherInfos() {
    cout << "Rectangle de " << longueur << " x " << largeur << endl;
    cout << "Surface totale : " << calculerSurface() << " m2" << endl;
}

