from collections import deque
from collections import defaultdict

EXIST = 1
NOT_EXIST = 0
HORIZONTAL = 0
VERTICAL = 1


def solution(board):
    def move(_next1, _next2, _count, _direction, _passing=(0, 0)):
        if not is_visited(visited, _next1, _next2) and is_possible_move(board, _next1, _next2) and board[_passing[0]][_passing[1]] == 0:
            q.append((_next1, _next2, _count+1, _direction))
            visited.update({(_next1, _next2): EXIST})

    n = len(board)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = defaultdict(lambda: NOT_EXIST)
    q = deque()
    q.append(((0, 0), (0, 1), 0, HORIZONTAL))

    while q:
        cur1, cur2, count, direction = q.popleft()
        cur1_y, cur1_x = cur1
        cur2_y, cur2_x = cur2

        if is_on_end_point(n, cur1, cur2):
            return count

        for dir in range(4):
            move((cur1_y+dy[dir], cur1_x+dx[dir]), (cur2_y+dy[dir], cur2_x+dx[dir]), count, direction)

        if direction == HORIZONTAL:
            move(cur1, (cur1_y+1, cur1_x), count, VERTICAL, (cur2_y+1, cur2_x))
            move(cur1, (cur1_y-1, cur1_x), count, VERTICAL, (cur2_y-1, cur2_x))
            move((cur2_y+1, cur2_x), cur2, count, VERTICAL, (cur1_y+1, cur1_x))
            move((cur2_y-1, cur2_x), cur2, count, VERTICAL, (cur1_y-1, cur1_x))
        else:
            move(cur1, (cur1_y, cur1_x+1), count, HORIZONTAL, (cur2_y, cur2_x+1))
            move(cur1, (cur1_y, cur1_x-1), count, HORIZONTAL, (cur2_y, cur2_x-1))
            move((cur2_y, cur2_x+1), cur2, count, HORIZONTAL, (cur1_y, cur1_x+1))
            move((cur2_y, cur2_x-1), cur2, count, HORIZONTAL, (cur1_y, cur1_x-1))


def is_visited(visited, spot1, spot2):
    return visited[(spot1, spot2)] == EXIST or visited[(spot2, spot1)] == EXIST


def is_possible_move(board, spot1, spot2):
    return is_in_field_robot(len(board), spot1, spot2) and is_in_road(board, spot1, spot2)


def is_in_road(board, spot1, spot2):
    return board[spot1[0]][spot1[1]] != 1 and board[spot2[0]][spot2[1]] != 1


def is_in_field_robot(n, spot1, spot2):
    return is_in_field(n, spot1[0], spot1[1]) and is_in_field(n, spot2[0], spot2[1])


def is_in_field(n, y, x):
    return 0 <= y < n and 0 <= x < n


def is_on_end_point(n, spot1, spot2):
    return (spot1[0] == n-1 and spot1[1] == n-1) or (spot2[0] == n-1 and spot2[1] == n-1)


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
