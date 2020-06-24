from collections import deque


def solution(n, computers):
    count = 0
    visited = [False for _ in range(n)]

    for node in range(n):
        if visited[node] is True:
            continue

        visited[node] = True
        q = deque([node])

        while q:
            cur_node = q.popleft()
            for next_node in range(n):
                if visited[next_node] or computers[cur_node][next_node] == 0 or next_node == cur_node:
                    continue
                visited[next_node] = True
                q.append(next_node)

        count += 1

    return count