class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for y in range(len(board)):
            for x in range(len(board[0])):
                if self.search(board, y, x, word, 0):
                    return True

        return False

    def search(self, board, y, x, word, idx):
        if idx == len(word):
            return True

        if y < 0 or x < 0 or y >= len(board) or x >= len(board[0]):
            return False

        if board[y][x] != word[idx]:
            return False

        now = board[y][x]
        board[y][x] = ''
        res = self.search(board, y + 1, x, word, idx + 1) \
              or self.search(board, y, x + 1, word, idx + 1) \
              or self.search(board, y - 1, x, word, idx + 1) \
              or self.search(board, y, x - 1, word, idx + 1)
        board[y][x] = now

        return res
