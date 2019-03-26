#include <bits/stdc++.h>
using namespace std;

int P[1001];
int D[1001];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;
    for (int i = 1; i <= N; i++)
        cin >> P[i];
    D[1] = P[1];
    for (int i = 2; i <= N; i++) {
        D[i] = P[i];
        for (int j = 1; j <= i - 1; j++)
            D[i] = max(D[i], D[j] + D[i - j]);
    }
    cout << D[N];
}
