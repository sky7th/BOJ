#N으로 표현
#best
def solution(N, number):
    S = [{N}]
    for i in range(2, 9):
        lst = [int(str(N)*i)]
        for X_i in range(0, int(i / 2)):
            for x in S[X_i]:
                for y in S[i - X_i - 2]:
                    lst.append(x + y)
                    lst.append(x - y)
                    lst.append(y - x)
                    lst.append(x * y)
                    if x != 0: lst.append(y // x)
                    if y != 0: lst.append(x // y)
        if number in set(lst):
            return i
        S.append(lst)
    return -1


#타일 장식물
def solution(N):
    if N == 1:
        return 4
    dp = [1,1]
    around = [4,6]
    for i in range(2, N):
        dp.append(dp[i-2] + dp[i-1])
        around.append(around[i-1] + dp[i]*2)
    return around.pop()


#정수 삼각형
def solution(t):
    for i in range(1,len(t)):
        for j in range(i+1):
            if j==0: 
                t[i][j] += t[i-1][j]
            elif j==i: 
                t[i][j] += t[i-1][j-1]
            else: 
                t[i][j] += max(t[i-1][j], t[i-1][j-1])
    return max(t[-1])


#등굣길
def solution(m, n, puddles):
    dp = [ [0 for _ in range(m+1)] for _ in range(n+1)]
    trap = [ [0 for _ in range(m+1)] for _ in range(n+1)]
    dp[1][1] = 1
    for x, y in puddles:
        trap[y][x] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if trap[i][j] == 1:
                continue
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n][m] % 1000000007


#카드 게임
def solution(left, right):
    len_l = len(left)
    len_r = len(right)
    D = [[0 for j in range(len_l+1)] for i in range(len_r+1)]
    
    for i in range(len_l):
        for j in range(len_r):
            if right[j] < left[i]:
                D[i+1][j+1] = D[i+1][j] + right[j]
            else:
                D[i+1][j+1] = max(D[i][j], D[i][j+1])

    return D[len_l][len_r]


#도둑질
def solution(money):
    length = len(money);
    dp = [0 for _ in range(length-1)];
    dp2= [0 for _ in range(length)];

    dp[0] = money[0];
    dp[1] = money[0];
    dp2[0] = 0;
    dp2[1] = money[1];
    for i in range(2, length-1):
        dp[i] = max(dp[i-2]+money[i],dp[i-1]);

    for i in range(2, length):
        dp2[i] = max(dp2[i-2]+money[i],dp2[i-1]);

    return max(dp[length-2],dp2[length-1]);
#다른 풀이
def solution(money):
    if len(money) == 3:
        return max(money)
    else:

        with0 = [money[0], money[1], money[0] + money[2], max(money[0], money[1]) + money[3]]
        wout0 = [money[1], money[2], money[1] + money[3]]
        for m in money[4:]:
            with0.append(max(with0[-2], with0[-3]) + m)
            wout0.append(max(wout0[-2], wout0[-3]) + m)

    return max(with0[-3], with0[-2], wout0[-1])


