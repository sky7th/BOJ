EMPTY = 0


def solution(board, moves):
    score = 0
    basket = []

    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] == EMPTY:
                continue

            score += put_doll_in_basket(basket, board[i][move - 1])
            board[i][move - 1] = EMPTY
            break

    return score


def put_doll_in_basket(basket, doll):
    if len(basket) > 0 and basket[-1] == doll:
        basket.pop()
        return 2

    basket.append(doll)
    return 0


print(solution([[1,1,1], [2,2,2], [3,3,3]], [1,2,1,2,1,2,1,2]))
