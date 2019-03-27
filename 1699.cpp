#include <bits/stdc++.h>
using namespace std;

int D[100001];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;
    for (int i = 1; i <= N; i++) {
        D[i] = i;
        for (int j = 1; j * j <= i; j++)
            D[i] = min(D[i], D[i - j * j] + 1);
    }
    cout << D[N];
}


// 더 빠른 답안
#include <stdio.h>

int isSquare[100001];
int isTwoSquare[100001];
int main(void) {
    for (int i = 1; i * i < 100001; i++)
        isSquare[i * i] = 1;
    for (int i = 1; i * i < 100001; i++) {
        for (int j = i; j * j + i * i < 100001; j++)
            isTwoSquare[i * i + j * j] = 1;
    }
    int N;
    scanf("%d", &N);
    if (isSquare[N])
        printf("1");
    else if (isTwoSquare[N])
        printf("2");
    else {
        for (int i = 1; i * i <= N; i++) {
            if (isTwoSquare[N - i * i]) {
                printf("3");
                return 0;
            }
        }
        printf("4");
    }
}