#include <bits/stdc++.h>
using namespace std;

int A[1001];
int D[1001];
int D_len[1001];

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> A[i];
    D[0] = A[0];
    D_len[0] = 1;
    int len = 1;
    for (int i = 1; i < N; ++i) {
        if (A[i] > D[len - 1]) {
            D[len++] = A[i];
            D_len[i] = len;
        } else {
            int idx = lower_bound(D, D + len, A[i]) - D;
            D[idx] = A[i];
            D_len[i] = idx + 1;
        }
    }
    cout << len << "\n";

    stack<int> S;
    for (int i = N - 1; i >= 0; i--) {
        if (D_len[i] == len) {
            S.push(A[i]);
            len--;
        }
    }
    while (!S.empty()) {
        cout << S.top() << " ";
        S.pop();
    }
}
