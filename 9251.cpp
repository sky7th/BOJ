#include <bits/stdc++.h>
using namespace std;

string S1, S2;
int cache[1001][1001];

int LCS(int idx1, int idx2) {
    if (idx1 == S1.size() || idx2 == S2.size())
        return 0;
    int& ret = cache[idx1][idx2];
    if (ret != -1) return ret;
    ret = 0;
    if (S1[idx1] == S2[idx2])
        ret = LCS(idx1+1, idx2+1) + 1;
    ret = max(ret, LCS(idx1+1, idx2));
    ret = max(ret, LCS(idx1, idx2+1));
    return ret;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> S1 >> S2;
    memset(cache, -1, sizeof(cache));
    cout << LCS(0, 0);
    return 0;
}