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
                        auto cur = Q.front();
                        Q.pop();
                        for (int dir = 0; dir < 4; dir++) {
                            int ny = cur.Y + dy[dir];
                            int nx = cur.X + dx[dir];
                            if (ny < 0 || ny >= N || nx < 0 || nx >= M)
                                continue;
                            if (field[ny][nx] == 1) {
                                Q.push(make_pair(ny, nx));
                                field[ny][nx] = 2;
                            }
                        }
                    }
                }
            }
        }
        cout << bug << '\n';
    }
}

/*
#include <bits/stdc++.h>
using namespace std;

int map[51][51];
int N, M, K;

void BFS(int p, int q) {
    if (map[p][q] != 1 || p<0 || p>=N || q<0 || q>=M) return;
    map[p][q] = 2;
    BFS(p - 1, q);
    BFS(p, q - 1);
    BFS(p, q + 1);
    BFS(p + 1, q);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T, X, Y;
    int wiggler;
    cin >> T;
    while(T--) {
        cin >> M >> N >> K;

        for (int i = 0; i < K; i++) {
            cin >> X >> Y;
            map[Y][X] = 1;
        }

        wiggler = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] == 1) {
                    wiggler++;
                    BFS(i, j);
                }
            }
        }
        cout << wiggler << endl;
    }

    return 0;
}

*/