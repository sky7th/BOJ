# 처음에 bfs로 풀었는데 시간 초과
from collections import deque

answer = 0


def solution(strs, t):
    q = deque()
    q.append(('', t, 0))

    while q:
        front_word, back_word, count = q.popleft()

        if front_word == t:
            return count

        for s in strs:
            if len(s) > len(back_word) or s != back_word[:len(s)]:
                continue
            q.append((front_word + s, back_word[len(s):], count + 1))

    return -1


# DP 풀이 2개
import math


def solution(strs, t):
    dp = [math.inf for _ in range(len(t))]
    for i in range(len(t) - 1, -1, -1):
        for k in range(1, 6):
            if t[i:i + k] in strs:
                is_out = False
                if i + k > len(t) - 1:
                    is_out = True
                dp[i] = min(dp[i], (0 if is_out else dp[i + k]) + 1)

    return -1 if dp[0] == math.inf else dp[0]


def solution(strs, t):
    size = len(t)
    dp = [-1]*(size+1)
    dp[0] = 0
    str_set = set(strs)

    for i in range(1, size+1):
        for j in range(1, 6):
            if i-j>=0 and t[i-j:i] in str_set and dp[i-j] != -1:
                if dp[i] == -1:
                    dp[i] = dp[i-j] + 1
                else:
                    dp[i] = min(dp[i], dp[i-j] + 1)
    return dp[-1]


print(solution(["ba", "na", "n", "a"], 'banana'))
