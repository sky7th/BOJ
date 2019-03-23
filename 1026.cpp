#include <bits/stdc++.h>
using namespace std;

int A[51];
int B[51];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> A[i];
    for (int i = 0; i < N; i++)
        cin >> B[i];
    sort(A, A + N);
    sort(B, B + N, greater<int>());
    int sum = 0;
    for (int i = 0; i < N; i++)
        sum += A[i] * B[i];
    cout << sum;
}