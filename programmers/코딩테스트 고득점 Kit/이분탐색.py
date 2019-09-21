#예산
# 1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정합니다.
# 2. 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정합니다. 
# 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정합니다.
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
# 입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 주어질 때, 
# 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 하도록 solution 함수를 작성해주세요.
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
