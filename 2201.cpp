#include <bits/stdc++.h>
using namespace std;
#define ll long long

ll D[90][2];

ll binary(int n, bool cur) {
    ll &ret = D[n][cur];
    if (ret != -1) return ret;
    if (n <= 1) return ret = n;
    ret = binary(n - 1, false);
    if (!cur) ret += binary(n - 1, true);
    return ret;
}

void skip(int n, bool cur, ll k) {
    cout << cur;
    if (n == 1) return;

    ll pivot = binary(n - 1, false);
    if (k < pivot)
        skip(n - 1, false, k);
    else
        skip(n - 1, true, k - pivot);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll K;
    ll sum = 0;
    cin >> K;
    memset(D, -1, sizeof(D));
    for (int i = 1;; i++) {
        if (binary(i, true) + sum >= K) {
            skip(i, 1, K - 1 - sum);
            break;
        }
        sum += binary(i, true);
    }
}