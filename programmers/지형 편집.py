# 파라메트릭 서치를 했지만 효율성이 전부 시간 초과
def solution(land, P, Q):
    flat_land = sum(land, [])
    left, right = min(flat_land), max(flat_land) + 1

    while left < right:
        mid = (left + right) // 2
        if get_cost(flat_land, P, Q, mid) > get_cost(flat_land, P, Q, mid+1):
            left = mid + 1
        else:
            right = mid

    return get_cost(flat_land, P, Q, left)


def get_cost(flat_land, P, Q, standard_height):
    cost = 0
    for height in flat_land:
        if height == standard_height:
            continue

        if height > standard_height:
            cost += Q * (height - standard_height)
        else:
            cost += P * (standard_height - height)

    return cost


print(solution([[4, 4, 3], [3, 2, 2], [2, 1, 0]], 5, 3))


# 전부 통과하는 답
# https://github.com/cottory/algorithm/blob/master/PROGRAMMERS/summer_winter11.cc