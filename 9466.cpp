#include <bits/stdc++.h>
using namespace std;

int S[100001];
bool visited[100001], finished[100001];
int cnt;

void dfs(int curr) {
    visited[curr] = true;
    int next = S[curr];
    if (visited[next]) {
        if (!finished[next]) {
            for (int temp = next; temp != curr; temp = S[temp])
                cnt++;
            cnt++;
        }
    } else
        dfs(next);
    finished[curr] = true;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        for (int i = 1; i <= N; i++) {
            cin >> S[i];
        }
        fill(visited, visited + N+1, false);
        fill(finished, finished + N+1, false);
        cnt = 0;
        for (int i = 1; i <= N; i++)
            if (!visited[i])
                dfs(i);
        cout << N - cnt << '\n';
    }
}
