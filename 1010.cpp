#include <bits/stdc++.h>
using namespace std;

int leg[31][31];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    for (int i = 1; i <= 30; i++) {
        leg[i][0] = 1;
        leg[i][i] = 1;
    }
    for (int i = 2; i <= 30; i++) {
        for (int j = 1; j <= i - 1; j++)
            leg[i][j] = leg[i-1][j] + leg[i-1][j-1];
    }
    int T;
    cin >> T;
    while (T--) {
        int N, M;
        cin >> N >> M;
        cout << leg[M][N] << '\n';
    }
}