#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<int> ns(n);

    for (int i = 0; i < n; i++) {
        cin >> ns[i];
    }

    int max_or = 0;

    for (int i = 0; i < n; ++i) {
        int res = 0;
        
        for (int j = i; j < n; ++j) {
            res |= ns[j];
            max_or = max(max_or, res);
        }
    }

    cout << max_or << endl;

    return 0;
}