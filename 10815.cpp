#include <bits/stdc++.h>
using namespace std;

int card[500001];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N, M;
    cin >> N;
    for (int i=0; i<N; i++)
        cin >> card[i];
    sort(card, card + N);
    cin >> M;
    while (M--) {
        int res;
        cin >> res;
        cout << binary_search(card, card + N, res);
    }
}
