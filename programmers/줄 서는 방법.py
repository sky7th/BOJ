from math import factorial


def solution(n, k):
    answer = []
    line = list(range(1, n+1))
    k = k-1

    while n > 0:
        n -= 1
        mok, k = divmod(k, factorial(n))
        answer.append(line.pop(mok))

    return answer


print(solution(3, 5))