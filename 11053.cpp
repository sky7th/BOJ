#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;
    vector<int> last(1, 0);
    int cur;
    for (int i = 0; i < N; i++) {
        cin >> cur;
        if (last.back() < cur)
            last.push_back(cur);
        else
            *lower_bound(last.begin(), last.end(), cur) = cur;
    }
    cout << last.size() - 1
}
