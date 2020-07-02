from collections import deque
import math

WALL = 1
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
ROAD_COST = 100
CORNER_COST = 500


def solution(board):
    visited = [[[[math.inf, math.inf, math.inf, math.inf] for _ in range(len(board)**2)] for _ in range(len(board[0]))] for _ in range(len(board))]
    q = deque()
    q.append((0, 0, 0, 0, RIGHT))
    q.append((0, 0, 0, 0, DOWN))

    while q:
        now_y, now_x, road_count, corner_count, now_direction = q.popleft()

        next_directions = get_left_and_right_direction(now_direction)
        for next_direction in next_directions:
            if now_y == 0 and now_x == 0:
                continue
            if not can_move(board, visited, now_y, now_x, corner_count + 1, next_direction):
                continue
            visited[now_y][now_x][corner_count + 1][next_direction] = road_count
            q.append((now_y, now_x, road_count, corner_count + 1, next_direction))

        next_y, next_x = get_front_location(now_direction, now_y, now_x)
        if not can_move(board, visited, next_y, next_x, corner_count, now_direction):
            continue
        visited[next_y][next_x][corner_count][now_direction] = road_count + 1
        q.append((next_y, next_x, road_count + 1, corner_count, now_direction))

    answer = math.inf
    for corner_count, road_counts in enumerate(visited[len(board)-1][len(board)-1]):
        min_road_count = min(road_counts)
        if min_road_count != math.inf:
            answer = min(answer, CORNER_COST*corner_count + ROAD_COST*min_road_count)

    return answer


def can_move(board, visited, next_y, next_x, corner_count, direction):
    if is_out_of_range(board, next_y, next_x, corner_count) or board[next_y][next_x] == WALL:
        return False
    if visited[next_y][next_x][corner_count][direction] != math.inf:
        return False
    return True


def is_out_of_range(board, y, x, corner_count):
    return x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or corner_count >= len(board)**2


def get_left_and_right_direction(direction):
    if direction == UP:
        return [LEFT, RIGHT]
    elif direction == RIGHT:
        return [UP, DOWN]
    elif direction == DOWN:
        return [RIGHT, LEFT]
    else:
        return [DOWN, UP]


def get_front_location(direction, now_y, now_x):
    if direction == UP:
        return now_y-1, now_x
    elif direction == RIGHT:
        return now_y, now_x+1
    elif direction == DOWN:
        return now_y+1, now_x
    else:
        return now_y, now_x-1


print(solution([[0,0,1],[0,0,0],[1,0,0]]))
