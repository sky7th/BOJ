#include <bits/stdc++.h>
using namespace std;

#define X first
#define Y second
typedef pair<int, int> PAIR;
vector<int> adj[10004]; 
int F[10004];
int mx = 0;
int N, M;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N >> M;
    while (M--) {
        int a, b;
        cin >> a >> b;
        adj[b].push_back(a);
    }
    for (int st = 1; st <= N; st++) {  // st를 해킹할것임
        bool isVisited[10005] = {
            0,
        };
        isVisited[st] = true;
        stack<int> S;
        S.push(st);
        int cnt = 1;
        while (!S.empty()) {
            int cur = S.top();
            S.pop();
            for (auto near : adj[cur]) {
                if (!isVisited[near]) {
                    isVisited[near] = true;
                    S.push(near);
                    cnt++;
                }
            }
        }
        F[st] = cnt;
        mx = max(mx, cnt);
    }
    for (int i = 1; i <= N; i++) {
        if (F[i] == mx)
            cout << i << ' ';
    }
}
