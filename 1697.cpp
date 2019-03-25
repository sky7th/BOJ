#include <bits/stdc++.h>
using namespace std;

int level[100001];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N, K;
    cin >> N >> K;
    queue<int> Q;
    Q.push(N);
    level[N] = 1;
    if (N == 1) {
        cout << '0';
        return 0;
    }
    while (1) {
        int cur = Q.front();
        Q.pop();
        int subin[3] = {cur + 1, cur - 1, cur * 2};
        for (int dir = 0; dir < 3; dir++) {
            if (subin[dir] < 0 || subin[dir] > 100000)
                continue;
            if (level[subin[dir]] != 0)
                continue;
            if (subin[dir] == K) {
                cout << level[cur];
                return 0;
            }
            level[subin[dir]] = level[cur] + 1;
            Q.push(subin[dir]);
        }
    }
}