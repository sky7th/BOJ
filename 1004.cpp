#include <bits/stdc++.h>
using namespace std;

bool isInner(int cx, int cy, int r, int x, int y) {
    return r * r > (cx - x) * (cx - x) + (cy - y) * (cy - y);
}
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    while (T--) {
        int x1, x2, y1, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        int n;
        cin >> n;

        int cnt = 0;
        for (int i = 0; i < n; i++) {
            int cx, cy, r;
            cin >> cx >> cy >> r;
            cnt += isInner(cx, cy, r, x1, y1) ^ isInner(cx, cy, r, x2, y2);
        }
        cout << cnt << '\n';
    }
    return 0;
}