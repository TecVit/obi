#include <bits/stdc++.h>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
  char v;
  float a, b;
  
  cin >> v >> a >> b;

  if (v == 'M') {
    cout << setprecision(4) << (a * b);
  } else if (v == 'D') {
    cout << setprecision(4) << (a / b);
  }

  return 0;
}