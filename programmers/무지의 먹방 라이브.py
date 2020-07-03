def solution(food_times, k):
    food_infos = [(time, idx) for idx, time in enumerate(food_times)]
    food_infos.sort()
    before_time = 0

    for idx, food_info in enumerate(food_infos):
        time, _ = food_info

        if time == before_time:
            continue

        leftover_food_count = (len(food_infos) - idx)
        time_height = (time - before_time)
        k = k - leftover_food_count * time_height

        if k < 0:
            last_leftover_food_infos = sorted(food_infos[idx:], key=lambda x: x[1])
            last_leftover_food_idx = last_leftover_food_infos[k % len(last_leftover_food_infos)][1]
            return last_leftover_food_idx + 1

        before_time = time

    return -1


print(solution([3, 1, 2], 5))