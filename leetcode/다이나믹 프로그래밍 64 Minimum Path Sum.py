class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        d = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        d[0][0] = grid[0][0]

        for i in range(0, len(d)):
            for j in range(0, len(d[0])):
                if i == 0 and j == 0: continue
                if i == 0:
                    d[i][j] = d[i][j - 1] + grid[i][j]
                elif j == 0:
                    d[i][j] = d[i - 1][j] + grid[i][j]
                else:
                    d[i][j] = min(d[i][j - 1], d[i - 1][j]) + grid[i][j]

        return d[len(d) - 1][len(d[0]) - 1]