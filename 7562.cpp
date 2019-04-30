#include <bits/stdc++.h>
using namespace std;

const int dy[8] = {-2, -1, 1, 2, -2, -1, 1, 2};
const int dx[8] = {-1, -2, -2, -1, 1, 2, 2, 1};
int visited[300][300];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int I;
        cin >> I;
        int sy, sx, ey, ex;
        cin >> sy >> sx >> ey >> ex;
        queue<int> Q;
        Q.push(sy * I + sx);
        visited[sy][sx] = true;
        int cnt = 0;
        while (1) {
            int find = 0;
            for (int i = 0; i < Q.size(); i++) {
                int cury = Q.front() / I;
                int curx = Q.front() % I;
                Q.pop();
                if (cury == ey && curx == ex) {
                    cout << cnt;
                    find = 0;
                    break;
                }
                for (int dir = 0; dir < 8; dir++) {
                    int nr = cury + dy[dir];
                    int nc = curx + dx[dir];
                    if (nr < 0 || nr >= I || nc < 0 || nc >= I)
                        continue;
                    if (visited[nr][nc])
                        continue;
                    visited[nr][nc] = 1;
                    Q.push(nr * I + nc);
                }
            }
            if (find)
                break;
            cnt++;
        }
    }
}