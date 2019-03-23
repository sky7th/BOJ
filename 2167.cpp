#include <bits/stdc++.h>
using namespace std;

int arr[301][301];
int D[301][301];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N, M;
    cin >> N >> M;
    for (int i = 1; i <= N; i++)
        for (int j = 1; j <= M; j++)
            cin >> arr[i][j];
    for (int i = 1; i <= N; i++) {
        D[i][1] = D[i - 1][1] + arr[i][1];
        for (int j = 2; j <= M; j++)
            D[i][j] = D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1] + arr[i][j];
    }
    int K;
    cin >> K;
    while (K--) {
        int i, j, x, y;
        cin >> i >> j >> x >> y;
        cout << D[x][y] - D[x][j - 1] - D[i - 1][y] + D[i - 1][j - 1] << '\n';
    }
}