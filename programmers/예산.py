def solution(budgets, M):
    answer = 0
    left = 0
    right = max(budgets)

    if sum(budgets) < M:
        return right

    while left < right:
        mid = (left + right) // 2
        res = 0
        for b in budgets:
            if mid > b:
                res += b
            else:
                res += mid

        if res <= M:
            left = mid + 1
            answer = mid
        else:
            right = mid

    return answer


print(solution([1,2,3,4,5,6,7,8,9,10], 56))