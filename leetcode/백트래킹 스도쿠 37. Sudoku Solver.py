from collections import defaultdict

# 시간 초과 !! 가지치기 할거 다한거 같은데.. 파이썬이라 느려서 그런거 같다. 자바로 다시 해보자
class Solution:
    isEnd = False

    def solveSudoku(self, board):
        self.backtrack(board, 0)
        print(board)

    def backtrack(self, board, idx):
        if idx == 81:
            return True
        y, x = divmod(idx, 9)
        if board[y][x] != '.':
            return self.backtrack(board, idx + 1)
        for i in range(1, 10):
            board[y][x] = str(i)
            if self.isValidSudoku(board):
                if self.backtrack(board, idx + 1):
                    return True
        board[y][x] = '.'
        return False


    def isValidSudoku(self, board):
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


solution = Solution()
solution.solveSudoku([[".",".",".",".",".","7",".",".","9"],[".","4",".",".","8","1","2",".","."],[".",".",".","9",".",".",".","1","."],[".",".","5","3",".",".",".","7","2"],["2","9","3",".",".",".",".","5","."],[".",".",".",".",".","5","3",".","."],["8",".",".",".","2","3",".",".","."],["7",".",".",".","5",".",".","4","."],["5","3","1",".","7",".",".",".","."]])