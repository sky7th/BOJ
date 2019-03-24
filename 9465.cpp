#include <bits/stdc++.h>
using namespace std;

int D[100001][2];
int sticker[100001][2];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        for (int i = 0; i < N; i++)
            cin >> sticker[i][0];
        for (int i = 0; i < N; i++)
            cin >> sticker[i][1];
        D[0][0] = sticker[0][0];
        D[0][1] = sticker[0][1];
        for (int i = 0; i < N; i++) {
            D[i][0] = max(D[i - 1][1] + sticker[i][0], D[i - 1][0]);
            D[i][1] = max(D[i - 1][0] + sticker[i][1], D[i - 1][1]);
        }
        cout << max(D[N - 1][0], D[N - 1][1]) << '\n';
    }
}