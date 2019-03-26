#include <bits/stdc++.h>
using namespace std;

int arr[21];
int res;
int N, S;

void func(int idx, int sum) {
    if (idx == N) {
        if (sum == S)
            res++;
        return;
    }
    func(idx + 1, sum);
    func(idx + 1, sum + arr[idx]);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N >> S;
    for (int i = 0; i < N; i++)
        cin >> arr[i];
    func(0, 0);
    
    cout << res + (!S ? -1 : 0);
}
