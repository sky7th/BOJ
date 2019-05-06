#include <bits/stdc++.h>
using namespace std;

int F, S, G, U, D;
int cache[1000001];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> F >> S >> G >> U >> D;
    queue<int> Q;
    Q.push(S);
    cache[S] = 1;
    while (!Q.empty()) {
        int cur = Q.front();
        Q.pop();
        if (cur == G) {
            cout << cache[cur] - 1;
            return 0;
        }
        int next[2] = {cur + U, cur - D};
        for (int i = 0; i < 2; i++) {
            if (next[i] < 0 || next[i] > F || cache[next[i]] != 0)
                continue;
            cache[next[i]] = cache[cur] + 1;
            Q.push(next[i]);
        }
    }
    cout << "use the stairs";
}
