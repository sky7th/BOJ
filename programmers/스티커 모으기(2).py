def solution(sticker):
    sticker_size = len(sticker)
    if sticker_size == 1:
        return sticker[0]

    dp1, dp2 = [0 for _ in range(sticker_size)], [0 for _ in range(sticker_size)]
    dp1[0], dp2[0] = sticker[0], 0
    dp1[1], dp2[1] = sticker[0], sticker[1]

    for i in range(2, sticker_size - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])

    for i in range(2, sticker_size):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    return max(dp1 + dp2)


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))