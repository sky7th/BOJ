def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            max_before = 0

            if j - 1 >= 0:
                max_before = max(max_before, triangle[i - 1][j - 1])

            if j <= i - 1:
                max_before = max(max_before, triangle[i - 1][j])

            triangle[i][j] += max_before

    return max(triangle[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
