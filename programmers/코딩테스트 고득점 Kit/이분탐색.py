#예산
def solution(budgets, M):
    answer=0
    left = 0
    right = max(budgets)

    while right >= left:
        mid = (left + right) // 2
        res = 0
        for b in budgets:
            if mid > b:
                res += b
            else:
                res += mid
        if res > M:
            right = mid-1
        else:
            left = mid+1
            answer = mid
    
    return answer
#좋은 풀이
def solution(budgets, M):
    budgets.sort()
    l = len(budgets)
    cap = 0
    for i, budget in enumerate(budgets):
        level = (budget - cap) * (l - i)
        if level <= M:
            cap = budget
            M -= level
        else:
            cap += M // (l - i)
            break
    return cap


#입국심사
#좋은 풀이
def solution(n, times):
    answer = 0
    start, end, mid = 1, times[-1] * n, 0

    while start < end:
        mid = (start + end) // 2
        total = 0
        for time in times:
            total += mid // time

        if total >= n:
            end = mid
        else:
            start = mid + 1
    answer = start
    return answer
