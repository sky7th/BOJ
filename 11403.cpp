#include <bits/stdc++.h>
using namespace std;

int graph[101][101];
int res[101][101];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;
    for (int i = 1; i <= N; i++)
        for (int j = 1; j <= N; j++)
            cin >> graph[i][j];
    for (int st = 1; st <= N; st++) {
        int visited[101] = { 0, };
        queue<int> Q;
        Q.push(st);
        while (!Q.empty()) {
            int cur = Q.front();
            Q.pop();
            for (int i = 1; i <= N; i++) {
                if (graph[cur][i] && !visited[i]) {
                    Q.push(i);
                    visited[i] = 1;
                    res[st][i] = 1;
                }
            }
        }
    }
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++)
            cout << res[i][j];
        cout << '\n';
    }
}
