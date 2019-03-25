#include <bits/stdc++.h>
using namespace std;

int coin[101];
int D[10001];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, k;
    cin >> n >> k;
    for (int i = 0; i < n; i++)
        cin >> coin[i];
    for (int i = 0; i <= k; i++)
        D[i] = 0x7ffffff;
    for (int i = 0; i < n; i++) {
        if (coin[i] > k)
            continue;
        D[coin[i]] = 1;
        for (int j = coin[i] + 1; j <= k; j++)
            D[j] = min(D[j], D[j - coin[i]] + 1);
    }
    if (D[k] == 0x7ffffff)
        D[k] = -1;
    cout << D[k];
}
