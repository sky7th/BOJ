EMPTY = '#'


def solution(m, n, board):
    board = [[[s] for s in row] for row in board]

    while True:
        removable_locations = find_removable_locations(board)
        if len(removable_locations) == 0:
            break
        remove_blocks(board, removable_locations)
        take_down_field(board)

    return count_empty_blocks(board)


def find_removable_locations(board):
    removable_locations = []
    for y in range(len(board) - 1):
        for x in range(len(board[0]) - 1):
            if is_removable(board, y, x):
                removable_locations.append((y, x))

    return removable_locations


def is_removable(board, y, x):
    block = board[y][x]
    return board[y][x] != EMPTY and board[y + 1][x] == block and board[y][x + 1] == block and board[y + 1][x + 1] == block


def remove_blocks(board, removable_locations):
    for location in removable_locations:
        y, x = location
        board[y][x], board[y + 1][x], board[y][x + 1], board[y + 1][x + 1] = EMPTY, EMPTY, EMPTY, EMPTY


def take_down_field(board):
    for x in range(len(board[0])):
        blocks = []
        for y in range(len(board)):
            if board[y][x] == EMPTY:
                continue
            blocks.append(board[y][x])
            board[y][x] = EMPTY

        for y in range(len(board)-len(blocks), len(board)):
            board[y][x] = blocks.pop(0)


def count_empty_blocks(board):
    count = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == EMPTY:
                count += 1

    return count


print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
