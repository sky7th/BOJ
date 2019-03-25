#include <bits/stdc++.h>
using namespace std;
#define MOD 10007

int D[1001];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    D[1] = 1;
    D[2] = 3;
    for (int i=3; i<=1000; i++)
        D[i] = (D[i-1] + 2*D[i-2]) % MOD;
    cout << D[n];
}
