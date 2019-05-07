#include <bits/stdc++.h>
using namespace std;

int weight[10000], cache[10000][2], N;
vector<int> adj[10000], result;
bool visited[10000], selected[10000];

int func(int root, int select) {
    int &ret = cache[root][select];
    if (ret != -1) return ret;
    visited[root] = true;
    int include = weight[root];
    int exclude = 0;
    for (int next : adj[root]) {
        if (!visited[next]) {
            include += func(next, false);
            exclude += func(next, true);
        }
    }
    visited[root] = false;  // ㅠㅡㅜ
    if (select && include > exclude) {
        selected[root] = true;
        return ret = include;
    }
    return ret = exclude;
}

void tracker(int root, bool select) {
    visited[root] = true;
    if (select && selected[root]) {
        result.push_back(root);
        for (int next : adj[root])
            if (!visited[next]) tracker(next, false);
    } else {
        for (int next : adj[root])
            if (!visited[next]) tracker(next, true);
    }
    visited[root] = false;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    memset(cache, -1, sizeof(cache));
    for (int i = 0; i < N; i++)
        cin >> weight[i];
    for (int i = 0; i < N - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u - 1].push_back(v - 1);
        adj[v - 1].push_back(u - 1);
    }
    cout << func(0, true) << '\n';
    tracker(0, true);
    sort(result.begin(), result.end());
    for (int node : result)
        cout << node + 1 << ' ';
}
