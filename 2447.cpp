#include <bits/stdc++.h>
using namespace std;
char board[2500][2500];
void star(int n, int y, int x) {
    if (n == 1) {
        board[y][x] = '*';
        return;
    }
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (i == 1 && j == 1) continue;
            star(n / 3, y + n / 3 * i, x + n / 3 * j);
        }
    }
}
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            board[i][j] = ' ';
    star(N, 0, 0);
    for (int i = 0; i < N; i++)
        cout << board[i] << '\n';
}