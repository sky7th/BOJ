#include <bits/stdc++.h>
using namespace std;

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
int field[51][51];

#define Y first
#define X second

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    while (T--) {
        int N, M, K;
        cin >> N >> M >> K;
        for (int i = 0; i < K; i++) {
            int y, x;
            cin >> y >> x;
            field[y][x] = 1;
        }
        int bug = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (field[i][j] == 1) {
                    bug++;
                    field[i][j] = 2;
                    queue<pair<int, int>> Q;
                    Q.push(make_pair(i, j));
                    while (!Q.empty()) {
                        auto f = Q.front();
                        Q.pop();
                        for (int dir = 0; dir < 4; dir++) {
                            if (f.Y + dy[dir] < 0 || f.Y + dy[dir] >= N || f.X + dx[dir] < 0 || f.X + dx[dir] >= M)
                                continue;
                            if (field[f.Y + dy[dir]][f.X + dx[dir]] == 1) {
                                Q.push(make_pair(f.Y + dy[dir], f.X + dx[dir]));
                                field[f.Y + dy[dir]][f.X + dx[dir]] = 2;
                            }
                        }
                    }
                }
            }
        }
        cout << bug << '\n';
    }
}