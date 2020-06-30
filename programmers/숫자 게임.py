from collections import deque


def solution(A, B):
    answer = 0

    A = sorted(A, reverse=True)
    B = deque(sorted(B, reverse=True))

    for num in A:
        if num >= B[0]:
            continue

        B.popleft()
        answer += 1

    return answer