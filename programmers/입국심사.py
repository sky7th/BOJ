def solution(n, times):
    left, right, mid = 0, times[-1]*n, 0

    while left < right:
        mid = (left + right) // 2
        total = 0

        for time in times:
            total += mid // time

        if total < n:
            left = mid + 1
        else:
            right = mid

    return left


print(solution(6, [7, 10]))
