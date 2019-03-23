#include <bits/stdc++.h>
using namespace std;

int A[100000];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> A[i];
    sort(A, A + N);
    int M;
    cin >> M;
    while (M--) {
        int num;
        cin >> num;
        cout << binary_search(A, A + N, num) << '\n';
    }
}