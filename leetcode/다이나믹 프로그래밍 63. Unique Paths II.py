class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        d = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        d[0][0] = 1

        for i in range(len(d)):
            for j in range(len(d[0])):
                if grid[i][j] == 1:
                    d[i][j] = 0
                else:
                    if i > 0: d[i][j] += d[i - 1][j]
                    if j > 0: d[i][j] += d[i][j - 1]

        return d[len(d) - 1][len(d[0]) - 1]