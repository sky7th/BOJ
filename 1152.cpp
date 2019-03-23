#include <bits/stdc++.h>
using namespace std;

char str[1000000];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int isEmpty = 1;
    int cnt = 0;
    gets(str);
    for (int i = 0; str[i]; i++) {
        if (str[i] == ' ')
            isEmpty = 1;
        else if (isEmpty) {
            isEmpty = 0;
            cnt++;
        }
    }
    cout << cnt;
}