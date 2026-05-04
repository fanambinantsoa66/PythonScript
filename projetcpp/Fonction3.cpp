#include <iostream>
#include <cmath>

using namespace std;

// FONCTION 1 : Pour calculer l'equation du second degre
void resoudreSecondDegre() {
    float a, b, c, delta, x1, x2;
    
    cout << "\n Resolution de ax^2 + bx + c = 0 :" << endl;

    do {
        cout << "Entrez a (different de 0) : ";
        cin >> a;
    } while (a == 0);

    cout << "Entrez b : "; cin >> b;
    cout << "Entrez c : "; cin >> c;

    delta = b * b - 4 * a * c;

    if (delta == 0) {
        cout << "L'equation admet une racine double : x = " << -b / (2 * a) << endl;
    } 
    else if (delta > 0) {
        x1 = (-b - sqrt(delta)) / (2 * a);
        x2 = (-b + sqrt(delta)) / (2 * a);
        cout << "L'equation admet deux racines distinctes : x1 = " << x1 << " et x2 = " << x2 << endl;
    } 
    else {
        cout << "Pas de solution reelle car delta negatif." << endl;
    }
}


// FONCTION 2 :Pour la table de multiplication
void afficherTableMultiplication() {
    int n;
    cout << "\n Table de multiplication " << endl;
    cout << "Entrez un entier : ";
    cin >> n;

   //Boucle pour l'iteration de i(1 a 10 )
    for (int i = 1; i <= 10; i++) {

   //Affichage du resultat table du nombre entrer
        cout << n << " x " << i << " = " << n * i << endl;
    }
}

// PROGRAMME PRINCIPAL
int main() {
    int choix;

    do {
        // Affichage du choix qui demande a l'utilisateur entrer son choix
        cout << " Choisir un de ces choix" << endl;
        cout << "1. Calculer equation second degre" << endl;
        cout << "2. Table de multiplication" << endl;
        cout << "3. Quitter" << endl;
        cout << "Entrer votre choix entre 1-3 : ";
        cin >> choix;

        // Traitement du choix en utilisant Switch
        switch (choix) {
            case 1:
                resoudreSecondDegre();
                break;
            case 2:
                afficherTableMultiplication();
                break;
            case 3:
                cout << "Au revoir !" << endl;
                break;
            default:
                cout << "Choix invalide, veuillez recommencer." << endl;
        }

    } while (choix != 3); // La boucle continue tant qu'on ne choisit pas 3

    return 0;
}

