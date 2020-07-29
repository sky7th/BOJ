class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for y in range(9):
            for x in range(9):
                if board[y][x] == '.': continue
                if not self.isValidHorizontal(board, y, x) or not self.isValidVertical(board, y,
                                                                                       x) or not self.isValidSquare(
                    board, y, x):
                    return False

        return True

    def isValidHorizontal(self, board, y, x):
        arr = list(filter(lambda x: x != '.', board[y]))
        return True if len(arr) == len(set(arr)) else False

    def isValidVertical(self, board, y, x):
        arr = list(filter(lambda x: x != '.', [board[i][x] for i in range(9)]))
        return True if len(arr) == len(set(arr)) else False

    def isValidSquare(self, board, y, x):
        arr = []
        a = y // 3
        b = x // 3
        for i in range(a * 3, a * 3 + 3):
            for j in range(b * 3, b * 3 + 3):
                if board[i][j] == '.': continue
                arr.append(board[i][j])

        return True if len(arr) == len(set(arr)) else False



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not self.isValidHorizontal(board) or not self.isValidVertical(board) or not self.isValidSquare(board):
            return False

        return True

    def isValidHorizontal(self, board):
        for i in range(9):
            visited = defaultdict(bool)
            for num in board[i]:
                if num == '.': continue
                if visited[num]: return False
                visited[num] = True
        return True

    def isValidVertical(self, board):
        for i in range(9):
            visited = defaultdict(bool)
            for num in [board[x][i] for x in range(9)]:
                if num == '.': continue
                if visited[num]: return False
                visited[num] = True
        return True

    def isValidSquare(self, board):
        for i in range(9):
            visited = defaultdict(bool)
            a, b = divmod(i, 3)
            for y in range(a * 3, a * 3 + 3):
                for x in range(b * 3, b * 3 + 3):
                    num = board[y][x]
                    if num == '.': continue
                    if visited[num]: return False
                    visited[num] = True
        return True