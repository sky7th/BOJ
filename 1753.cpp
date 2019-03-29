#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
#define
int dist[20001];
vector<pair<int, int>> edge[20001];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int V, E, st;
    cin >> V >> E;
    cin >> st;
    for (int i = 0; i <= V; i++)
        dist[i] = 987654321;
    while (E--) {
        int u, v, w;
        cin >> u >> v >> w;
        edge[u].push_back(make_pair(v, w));
    }
    dist[st] = 0;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push(make_pair(0, st));
    while (!pq.empty()) {
        int my_dist = pq.top().X;
        int current = pq.top().Y;
        pq.pop();
        if (dist[current] < my_dist)
            continue;
        for (int i = 0; i < edge[current].size(); i++) {
            if (dist[edge[current][i].X] > my_dist + edge[current][i].Y) {
                dist[edge[current][i].X] = my_dist + edge[current][i].Y;
                pq.push(make_pair(dist[edge[current][i].X], edge[current][i].X));
            }
        }
    }
    for (int i = 1; i <= V; i++) {
        if (dist[i] == 987654321)
            cout << "INF" << '\n';
        else
            cout << dist[i];
    }
}