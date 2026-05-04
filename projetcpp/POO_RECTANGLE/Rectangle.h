#ifndef RECTANGLE_H
#define RECTANGLE_H

class Rectangle {
private:
    double longueur;
    double largeur;

public:
    // Constructeur
    Rectangle(double L, double l);

    // Méthodes
    double calculerSurface();
    void afficherInfos();
};

#endif

