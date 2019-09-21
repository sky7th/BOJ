#N으로 표현
# 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.
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
# 1. 언제든지 왼쪽 카드만 통에 버릴 수도 있고 왼쪽 카드와 오른쪽 카드를 둘 다 통에 버릴 수도 있다. 이때 얻는 점수는 없다.
# 2. 오른쪽 카드에 적힌 수가 왼쪽 카드에 적힌 수보다 작은 경우에는 오른쪽 카드만 통에 버릴 수도 있다. 오른쪽 카드만 버리는 경우에는 오른쪽 카드에 적힌 수만큼 점수를 얻는다.
# 3. (1)과 (2)의 규칙에 따라 게임을 진행하다가 어느 쪽 더미든 남은 카드가 없다면 게임이 끝나며 그때까지 얻은 점수의 합이 최종 점수가 된다
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
# 각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보가 울립니다.
# 각 집에 있는 돈이 담긴 배열 money가 주어질 때, 도둑이 훔칠 수 있는 돈의 최댓값을 return 하도록 solution 함수를 작성하세요.
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


