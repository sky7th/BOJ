from collections import defaultdict
from collections import deque


def solution(n, vertex):
    graph = defaultdict(list)
    visited = defaultdict(bool)
    dists = defaultdict(int)

    for edge in vertex:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    q = deque([1])
    visited[1] = True

    while q:
        now_node = q.popleft()
        for next_node in graph[now_node]:
            if visited[next_node] is True:
                continue

            visited[next_node] = True
            dists[next_node] = dists[now_node] + 1
            q.append(next_node)

    dists = list(dists.values())

    return dists.count(max(dists))