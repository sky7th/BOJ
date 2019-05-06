#include <bits/stdc++.h>
using namespace std;
#define PAIR pair<int, int>
#define Y first
#define X second
int dy[4] = {1, -1, 0, 0};
int dx[4] = {0, 0, 1, -1};
int N, M;
string field[51];
int cache[51][51];

int BFS(int y, int x) {
    memset(cache, 0, sizeof(cache));
    queue<PAIR> Q;
    int res = 0;
    Q.push({y, x});
    cache[y][x] = 1;
    while (!Q.empty()) {
        auto cur = Q.front();
        Q.pop();
        res = max(res, cache[cur.Y][cur.X]);
        for (int dir = 0; dir < 4; dir++) {
            int ny = cur.Y + dy[dir];
            int nx = cur.X + dx[dir];
            if (ny < 0 || ny >= N || nx < 0 || nx >= M)
                continue;
            if (field[ny][nx] != 'L' || cache[ny][nx] != 0)
                continue;
            Q.push({ny, nx});
            cache[ny][nx] = cache[cur.Y][cur.X] + 1;
        }
    }
    return res - 1;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N >> M;
    for (int i = 0; i < N; i++) {
        cin >> field[i];
    }
    int res = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (field[i][j] == 'L')
                res = max(res, BFS(i, j));
        }
    }
    cout << res;
}
