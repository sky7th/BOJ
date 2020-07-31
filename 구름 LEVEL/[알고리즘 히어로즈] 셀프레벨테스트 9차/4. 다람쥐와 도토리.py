# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N, M = list(map(int, input().split()))
x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))

# N, M의 최대값이 5000000... 시간초과남.. 좀 더 고민해보자.
def solution():
    ret = 0
    if x1 <= x2 and y1 <= y2:
        ret += dp(0, 0, y1 + 1, x1 + 1)
        ret *= dp(y1, x1, M + 1, N + 1, True)
    elif x1 >= x2 and y1 >= y2:
        ret += dp(0, 0, y1 + 1, x1 + 1, True)
        ret *= dp(y1, x1, M + 1, N + 1)
    else:
        ret += dp(0, 0, y1 + 1, x1 + 1)
        ret *= dp(y1, x1, M + 1, N + 1)

    return ret % 1000000007


def dp(start_y, start_x, M, N, isExistTrap=False):
    d = [[0 for _ in range(N)] for _ in range(M)]
    d[start_y][start_x] = 1
    for y in range(start_y, M):
        for x in range(start_x, N):
            if isExistTrap:
                if y == y2 and x == x2:
                    d[y][x] = 0
                    continue
            if x > 0: d[y][x] += d[y][x - 1] % 1000000007
            if y > 0: d[y][x] += d[y - 1][x] % 1000000007

    return d[M - 1][N - 1]


print(solution())