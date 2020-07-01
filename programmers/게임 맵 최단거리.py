from collections import deque

WALL = 0


def solution(maps):
    n, m = len(maps), len(maps[0])
    dys = [1, 0, -1, 0]
    dxs = [0, 1, 0, -1]
    q = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]

    q.append((0, 0, 1))
    visited[0][0] = True

    while q:
        now_y, now_x, count = q.popleft()

        if now_y == n - 1 and now_x == m - 1:
            return count

        for dy, dx in zip(dys, dxs):
            next_y, next_x = now_y + dy, now_x + dx

            if is_out_of_maps(n, m, next_y, next_x) or is_wall(maps, next_y, next_x) \
                    or visited[next_y][next_x]:
                continue

            visited[next_y][next_x] = True
            q.append((next_y, next_x, count + 1))

    return -1


def is_out_of_maps(n, m, y, x):
    return y < 0 or y >= n or x < 0 or x >= m


def is_wall(maps, y, x):
    return maps[y][x] == WALL


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))