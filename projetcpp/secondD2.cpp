#include <iostream>
#include <cmath> // Utilisation de cmath pour sqrt()

using namespace std;
// Declaration de la fonction en dehors du main
void resoudreSecondDegre(float a, float b, float c) {
    float delta, x, x1, x2;

    delta = b * b - 4 * a * c;

    cout << "Solution de l'equation : " << endl;

    if (delta == 0) {
        x = -b / (2 * a);
        cout << "L'equation admet une racine double : x = " << x << endl;
    } 
    else if (delta > 0) {
        // Calcul de racines diqtinctes 
        x1 = (-b - sqrt(delta)) / (2 * a);
        x2 = (-b + sqrt(delta)) / (2 * a);
        cout << "les desux racines reelles : " << endl;
        cout << "x1 = " << x1 << endl;
        cout << "x2 = " << x2 << endl;
    } 
    else {
        cout << "Pas de solution car delta < 0)." << endl;
    }
}

int main() {
    float a, b, c;

    cout << "Resolution de l'equation ax^2 + bx + c = 0" << endl;

    // Boucle pour assurer que la valeyr de a n'est pas nul
    do {
        cout << "Entrez a (different de 0) : ";
        cin >> a;
        if (a == 0) {
            cout << "Erreur : 'a' ne peut pas être nul dans une équation du second degré." << endl;
        }
    } while (a == 0);

    cout << "Entrez b : ";
    cin >> b;
    cout << "Entrez c : ";
    cin >> c;

    // Appel de la fonction
    resoudreSecondDegre(a, b, c);

    return 0;
}
 // Fonction pour le table de multiplication
void TableMultiplication() {
    int n;
    // Ecrire le nombre pour calculer sa tqble
    cout <<"Entrez un nombre pour calculer sa Table : ";
    cin >> n;

    cout << "\n Table de multiplication de " <<n << "  >

    // Boucle de 1 => 10
    for (int i = 1; i <= 10; i++) {
        int d= n*i;
    // Affichage du table
        cout << n << " x " << i << " = " <<d << endl;
    }
    cout << "------------------------" << endl;
}

int main() {
    // Appel de la fonction
    TableMultiplication();

    return 0 ;
}
