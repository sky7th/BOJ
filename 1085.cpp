#include <bits/stdc++.h>
using namespace std;

int escape(int a, int b, int c, int d) {
    int minVal = a;
    minVal = min(minVal, b);
    minVal = min(minVal, c);
    minVal = min(minVal, d);
    return minVal;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int x, y, w, h;
    cin >> x >> y >> w >> h;
    cout << escape(x, w-x, y, h-y);
}