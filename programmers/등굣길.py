def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    trap = [[0 for _ in range(m)] for _ in range(n)]
    HOLE = 1
    dp[0][0] = 1

    for x, y in puddles:
        trap[y - 1][x - 1] = HOLE

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue

            if trap[i][j] == HOLE:
                continue

            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[n - 1][m - 1] % 1000000007


print(solution(4, 3, [[2, 2]]))
