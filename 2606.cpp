#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> birus;
bool visited[101];
int ans;

void dfs(int n) {
    visited[n] = true;
    ans++;
    for (int m = 0; m < birus[n].size(); m++) {
        if (!visited[birus[n][m]]) dfs(birus[n][m]);
    }
    return;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int C, N, from, to;
    cin >> C >> N;
    birus.resize(C + 1);
    for (int i = 0; i < N; i++) {
        cin >> from >> to;
        birus[from].push_back(to);
        birus[to].push_back(from);
    }
    dfs(1);
    cout << ans - 1;
}
