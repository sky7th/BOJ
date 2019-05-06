#include <bits/stdc++.h>
using namespace std;

vector<int> family[101];
int N, M, node1, node2;
int cache[101];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    cin >> node1 >> node2;
    cin >> M;
    for (int i = 0; i < M; i++) {
        int parent, child;
        cin >> parent >> child;

        family[parent].push_back(child);
        family[child].push_back(parent);
    }
    queue<int> Q;
    Q.push(node1);
    while (!Q.empty()) {
        int cur = Q.front();
        Q.pop();
        if (cur == node2) {
            cout << cache[node2];
            return 0;
        }
        for (int i = 0; i < family[cur].size(); i++) {
            int next = family[cur][i];
            if (cache[next]) continue;
            Q.push(next);
            cache[next] = cache[cur] + 1;
        }
    }
    cout << -1 << '\n';
}
