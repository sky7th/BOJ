#include <bits/stdc++.h>
using namespace std;

long long D[100][2];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;
    D[1][0] = 1;
    D[1][1] = 1;
    for (int i = 2; i <= N; i++) {
        D[i][0] = D[i - 1][0] + D[i - 1][1];
        D[i][1] = D[i - 1][0];
    }
    cout << D[N][1];
}