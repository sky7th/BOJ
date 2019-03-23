#include <bits/stdc++.h>
using namespace std;

void star(int n) {
    while (n--)
        cout << "*";
}

void extra(int n) {
    while (n--)
        cout << " ";
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;
    for (int i = 1; i <= N; i++) {
        extra(N - i);
        star(2 * i - 1);
        cout << '\n';
    }
}