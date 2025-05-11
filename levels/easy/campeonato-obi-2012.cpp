#include <iostream>
using namespace std;

int main() {
    int cv, ce, cs;
    int fv, fe, fs;
    cin >> cv >> ce >> cs >> fv >> fe >> fs;

    int pc = (cv * 3) + (ce * 1);
    int pf = (fv * 3) + (fe * 1);

    if (pc > pf) {
        cout << 'C';
    } else if (pf > pc) {
        cout << 'F';
    } else {
        if (cs > fs) {
            cout << 'C';
        } else if (fs > cs) {
            cout << 'F';
        } else {
            cout << '=';
        }
    }

    return 0;
}