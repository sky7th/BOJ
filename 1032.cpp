#include <bits/stdc++.h>
using namespace std;

char str[51][51];
char res[51];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> str[i];
    int len = strlen(str[0]);
    int cnt = 0;
    for (int i = 0; i < len; i++) {
        res[i] = str[0][i];
        for (int j = 0; j < N; j++) {
            if (str[0][i] != str[j][i]) {
                res[i] = '?';
                break;
            }
        }
    }
    cout << res;
}