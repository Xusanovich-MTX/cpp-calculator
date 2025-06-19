#include <iostream>
using namespace std;

int main() {
    double a, b;
    char amal;

    cout << "Birinchi sonni kiriting: ";
    cin >> a;

    cout << "Amalni kiriting (+, -, *, /): ";
    cin >> amal;

    cout << "Ikkinchi sonni kiriting: ";
    cin >> b;

    double natija;

    switch (amal) {
        case '+': natija = a + b; break;
        case '-': natija = a - b; break;
        case '*': natija = a * b; break;
        case '/':
            if (b != 0) natija = a / b;
            else {
                cout << "0 ga bo‘lib bo‘lmaydi!" << endl;
                return 1;
            }
            break;
        default:
            cout << "Noto‘g‘ri amal!" << endl;
            return 1;
    }

    cout << "Natija: " << natija << endl;

    return 0;
}
