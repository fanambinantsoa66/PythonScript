#include <iostream>

using namespace std;

// Fonction qui demande le nombre et affiche sa table

void TableMultiplication() {
    int n;

    cout<<"Entrez un nombre pour calculer sa table : ";
    cin >> n;

    cout << "\n Table de multiplication de " <<n << "  " << endl;

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

