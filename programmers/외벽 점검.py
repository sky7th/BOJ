# 첫 번째 풀이 (지저분)
from itertools import permutations


def solution(n, weaks, dists):
    answer = []
    weaks_len = len(weaks)
    all_weaks = weaks + [n + i for i in weaks]
    dists_perm = list(permutations(dists))

    for i in range(0, len(all_weaks) - weaks_len):
        weak = all_weaks[i:i + weaks_len]

        for dists in dists_perm:
            weak_index = 0
            friend_count = 0
            for dist in dists:
                standard = weak_index
                for j in range(weak_index, len(weak)):
                    if weak[j] > weak[standard] + dist:
                        break
                    weak_index = j

                weak_index += 1
                friend_count += 1

                if weak_index == len(weak):
                    break

            if weak_index != len(weak):
                continue

            answer.append(friend_count)

    if len(answer) == 0:
        return -1

    return min(answer)


# 두 번째 풀이 (시간 반으로 줄임)
from itertools import permutations


def solution(n, weak, dist):
    weak_len = len(weak)
    answer = len(dist) + 1
    weak += [n + i for i in weak]

    for i in range(weak_len):
        _weak = [weak[j] for j in range(i, i + weak_len)]

        for _dist in permutations(dist):
            weak_idx, dist_idx, friend_count = 0, 0, 1

            for idx in range(1, weak_len):
                if _weak[idx] > _weak[weak_idx] + _dist[dist_idx]:
                    friend_count += 1
                    weak_idx = idx

                    if friend_count > len(_dist):
                        break

                    dist_idx += 1

            answer = min(answer, friend_count)

    return -1 if answer > len(dist) else answer


# 좋은 풀이 (최선의 방법부터 시도)
from collections import deque


def solution(n, weak, dist):
    dist.sort(reverse=True)
    q = deque([weak])
    visited = set()
    visited.add(tuple(weak))

    for i in range(len(dist)):
        d = dist[i]
        for _ in range(len(q)):
            current = q.popleft()
            for p in current:
                l = p
                r = (p + d) % n
                if l < r:
                    temp = tuple(filter(lambda x: x < l or x > r, current))
                else:
                    temp = tuple(filter(lambda x: x < l and x > r, current))

                if len(temp) == 0:
                    return (i + 1)

                if temp not in visited:
                    visited.add(temp)
                    q.append(list(temp))
    return -1


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
