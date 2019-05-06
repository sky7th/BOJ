#include <bits/stdc++.h>
using namespace std;
#define Y first
#define X second
#define PAIR pair<int, int>
int dy[4] = { 0, 0, 1, -1 };
int dx[4] = { 1, -1, 0, 0 };
int height[101][101];
int safe[101][101];
int N;

int rain() {
    int cnt = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (safe[i][j]) {
                cnt++;
                safe[i][j] = false;
                queue<PAIR> Q;
                Q.push({i, j});
                while (!Q.empty()) {
                    auto cur = Q.front();
                    Q.pop();
                    for (int dir = 0; dir < 4; dir++) {
                        int ny = cur.Y + dy[dir];
                        int nx = cur.X + dx[dir];
                        if (nx < 0 || nx >= N || ny < 0 || ny >= N)
                            continue;
                        if (safe[ny][nx]) {
                            Q.push({ny, nx});
                            safe[ny][nx] = false;
                        }
                    }
                }
            }
        }
    }
    return cnt;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++)
            cin >> height[i][j];
    }
    int mx = 1;
    for (int h = 1; h <= 100; h++) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                safe[i][j] = (height[i][j] > h);
            }
        }
        mx = max(mx, rain());
    }
    cout << mx;
}
