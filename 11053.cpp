// N*N
#include <bits/stdc++.h>
using namespace std;

int A[1001];
int D[1001];
int N, res;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> A[i];
    for (int i = 0; i < N; i++) {
        int len = 0;
        for (int j = 0; j < i; j++) {
            if (A[j] < A[i])
                len = max(len, D[j]);
        }
        D[i] = len + 1;
        res = max(res, D[i]);
    }
    cout << res;
}

// logN* N
#include <bits/stdc++.h>
using namespace std;

int A[1001];
int D[1001];

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;
    for (int i=0; i<N; i++) 
        cin >> A[i];
    D[0] = A[0];
    int len = 1; 
    for(int i = 1; i < N; ++i) {
        if (A[i] > D[len-1])
            D[len++] = A[i];
        else
            *lower_bound(D, D + len, A[i]) = A[i];
    }
    cout << len;
    return 0;
}