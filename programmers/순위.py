# 시간 초과
from collections import defaultdict


def solution(n, results):
    win_dict, lose_dict = defaultdict(set), defaultdict(set)
    for winner, loser in results:
        win_dict[winner].add(loser)
        lose_dict[loser].add(winner)

    can_be_ranked_user_count = 0
    for user_id in range(1, n+1):
        if len(get_all_opponents(win_dict, user_id)) + len(get_all_opponents(lose_dict, user_id)) == n-1:
            can_be_ranked_user_count += 1

    return can_be_ranked_user_count


def get_all_opponents(result_dict, user_id):
    opponents = result_dict[user_id].copy()
    for opponent in result_dict[user_id]:
        opponents.update(get_all_opponents(result_dict, opponent))

    return opponents


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))

# 통과
from collections import defaultdict


def solution(n, results):
    win_dict, lose_dict = defaultdict(set), defaultdict(set)
    for winner, loser in results:
        win_dict[winner].add(loser)
        lose_dict[loser].add(winner)

    for user_id in range(1, n+1):
        for opponent in win_dict[user_id]:
            lose_dict[opponent].update(lose_dict[user_id])

        for opponent in lose_dict[user_id]:
            win_dict[opponent].update(win_dict[user_id])

    can_be_ranked_user_count = 0
    for user_id in range(1, n+1):
        if len(win_dict[user_id]) + len(lose_dict[user_id]) == n-1:
            can_be_ranked_user_count += 1

    return can_be_ranked_user_count


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))

