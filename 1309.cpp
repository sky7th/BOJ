#include <bits/stdc++.h>
using namespace std;
#define MOD 9901

int D[100001];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;
    D[0] = 1;
    D[1] = 3;
    int sum = D[0];
    for (int i = 2; i <= 100000; i++) {
        D[i] = (D[i - 1] + 2 * sum + 2) % MOD;
        sum = (sum + D[i - 1]) % MOD;
    }
    cout << D[N];
}
