#include <bits/stdc++.h>
using namespace std;

vector<int> birus[101];
bool visited[101];
int ans;

void dfs(int n) {
    visited[n] = true;
    ans++;
    for (int i = 0; i < birus[n].size(); i++) { 
        if (!visited[birus[n][i]]) dfs(birus[n][i]);
    }
    return;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int C, N, from, to;
    cin >> C >> N;
    for (int i = 0; i < N; i++) {
        cin >> from >> to;
        birus[from].push_back(to);
        birus[to].push_back(from);
    }
    dfs(1);
    cout << ans - 1;
}
