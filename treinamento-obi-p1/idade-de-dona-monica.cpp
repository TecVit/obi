#include <bits/stdc++.h>
using namespace std;

int main() {
    int monica, filho1, filho2, filho3;
    cin >> monica >> filho1 >> filho2;

    filho3 = monica - filho1 - filho2;

    if (filho1 > filho2 and filho1 > filho3) {
        cout << filho1;
    } else if (filho2 > filho1 and filho2 > filho3) {
        cout << filho2;
    } else {
        cout << filho3;
    }
    
}