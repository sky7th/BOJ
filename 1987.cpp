#include <bits/stdc++.h>
using namespace std;

char board[21][21];
bool visited[26];
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};
int max_depth;
int R, C;

void dfs(int r, int c, int depth) {
    max_depth = max(max_depth, depth);
    visited[board[r][c] - 'A'] = true;
    for (int dir = 0; dir < 4; dir++) {
        if (r + dx[dir] < 0 || r + dx[dir] >= R || c + dy[dir] < 0 || c + dy[dir] >= C)
            continue;
        if (visited[board[r + dx[dir]][c + dy[dir]] - 'A'])
            continue;
        dfs(r + dx[dir], c + dy[dir], depth + 1);
    }
    visited[board[r][c] - 'A'] = false;
}
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> R >> C;
    for (int i = 0; i < R; i++)
        cin >> board[i];
    dfs(0, 0, 1);
    cout << max_depth;
}
