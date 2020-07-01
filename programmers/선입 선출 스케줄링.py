# Time을 증가시켜 가며 코어 전부를 검사
# 최악의 경우 O(n * core 개수) 근접
def solution(n, cores):
    time = 0

    while True:
        for core in cores:
            if time % core == 0:
                n -= 1

            if n == 0:
                return core

        time += 1

from heapq import heappush, heappop


# 우선순위 큐 사용
# O(n)
def solution(n, cores):
    n -= len(cores)
    time = 0
    pq = []

    for idx, core in enumerate(cores):
        heappush(pq, (core, idx))

    while n > 0:
        while pq[0][0] == time:
            end_time, idx = heappop(pq)
            n -= 1

            if n == 0:
                return idx + 1

            heappush(pq, (time + cores[idx], idx))

        time += 1


# Parametric Search를 사용한 풀이2
# O(log n)
def solution(n, cores):
    if n <= len(cores):
        return n

    min_core = min(cores)
    min_time = n // len(cores) * min_core
    max_time = n * min_core

    while min_time < max_time:
        count = 0
        available_count = 0
        mid_time = (min_time + max_time) // 2

        for core in cores:
            count += (mid_time // core) + 1
            if mid_time % core == 0:
                available_count += 1
                count -= 1

        if count >= n:
            max_time = mid_time
            continue

        if count + available_count < n:
            min_time = mid_time + 1
            continue

        for idx, core in enumerate(cores):
            if mid_time % core == 0:
                count += 1

            if count == n:
                return idx + 1


# Parametric Search를 사용한 풀이2
def solution(n, cores):
    left = 0
    right = n * 10000
    rest = n - len(cores)

    while left < right:
        mid = (left + right) // 2
        completed_work = 0

        for core in cores:
            completed_work += mid // core

        if completed_work < rest:
            left = mid + 1
        else:
            right = mid

    for i in cores:
        rest -= (left - 1) // i

    idx = 0
    while rest != 0:
        if left % cores[idx] == 0:
            rest -= 1

        idx += 1

    return idx


print(solution(8, [1, 2, 3]))
