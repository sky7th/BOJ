# 매우 신기 !
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        matrix.reverse()
        for y in range(N):
            for x in range(y + 1, N):
                matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]