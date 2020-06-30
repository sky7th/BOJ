count = 0
board = [0] * 12


def solution(n):
    put_queen(n, 0)

    return count


def put_queen(n, row):
    global count, board

    if row == n:
        count += 1
        return

    for col in range(n):
        board[row] = col
        if is_possible_zone(row):
            put_queen(n, row + 1)


def is_possible_zone(row):
    for i in range(row):
        if board[i] == board[row] or abs(board[i] - board[row]) == row - i:
            return False
    return True


print(solution(4))


