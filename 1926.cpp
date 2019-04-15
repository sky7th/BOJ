#include <bits/stdc++.h>
using namespace std;
#define Y first
#define X second
int board[505][505];
bool vis[505][505];
int n, m;
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> board[i][j];
    int mx = 0;
    int num = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (board[i][j] == 0 || vis[i][j]) continue;
            num++;
            vis[i][j] = 1;
            queue<pair<int, int> > Q;
            Q.push({i, j});
            int area = 0;
            while (!Q.empty()) {
                area++;
                auto cur = Q.front();
                Q.pop();
                for (int dir = 0; dir < 4; dir++) {
                    int ny = cur.Y + dy[dir];
                    int nx = cur.X + dx[dir];
                    if (ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
                    if (vis[ny][nx] || board[ny][nx] != 1) continue;
                    vis[ny][nx] = 1;
                    Q.push({ny, nx});
                }
            }
            mx = max(mx, area);
        }
    }
    cout << num << '\n'
         << mx;
}