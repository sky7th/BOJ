#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    if (T % 10 != 0) {
        cout << '-1';
        return 0;
    }
    int five = T / 300;
    T -= five * 300;
    int one = T / 60;
    T -= one * 60;
    cout << five << one << T;
}
