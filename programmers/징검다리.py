def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    left, right = 0, distance + 1

    while left < right:
        mid = (left + right) // 2
        count = 0
        now_rock = 0

        for rock in rocks:
            if rock - now_rock <= mid:
                count += 1
            else:
                now_rock = rock

        if count <= n:
            left = mid + 1
        else:
            right = mid

    return left


print(solution(25, [2, 14, 11, 21, 17], 2))
