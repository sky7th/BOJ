#include <bits/stdc++.h>
using namespace std;

int con(int n) {
    if (n == 0)
        return 10;
    return n;
}

int pow(int a, int b) {
    if (b == 1)
        return con(a % 10);
    int tmp = pow(a, b / 2);
    if (b % 2 == 0)
        return con(tmp * tmp % 10);
    if (b % 2 != 0)
        return con(tmp * tmp * a % 10);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    while (T--) {
        int a, b;
        cin >> a >> b;
        cout << pow(a, b) << '\n';
    }
}