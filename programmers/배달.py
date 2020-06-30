from collections import defaultdict
from collections import deque
import math


def solution(N, road, K):
    d = defaultdict(list)
    town_lens = [math.inf for _ in range(N + 1)]

    for way in road:
        a, b, dist = way
        d[a].append((b, dist))
        d[b].append((a, dist))

    q = deque()
    q.append(1)
    town_lens[1] = 0

    while q:
        now_town = q.popleft()

        for next_town, next_dist in d[now_town]:
            dist = town_lens[now_town] + next_dist

            if dist >= town_lens[next_town] or dist > K:
                continue

            town_lens[next_town] = dist
            q.append(next_town)

    return len([n for n in town_lens if n <= K])


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))