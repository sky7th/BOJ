#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;
    int p = 2;
    for (int i=2; i*i <= N; i++) {
        while (N % i == 0) {
            cout << i << '\n';
            N /= i;
        }
    }
    if (N != 1)
        cout << N;
}