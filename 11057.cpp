#include <bits/stdc++.h>
using namespace std;
#define MOD 10007

int D[1006][10];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;
    for (int i = 0; i < 10; i++)
        D[1][i] = 1;
    for (int i = 2; i <= N; i++) {
        for (int j = 0; j < 10; j++) {
            for (int k = 0; k <= j; k++)
                D[i][j] = (D[i][j] + D[i - 1][k]) % MOD;
        }
    }
    int res = 0;
    for (int i = 0; i < 10; i++)
        res = (res + D[N][i]) % MOD;
    cout << res;
}
