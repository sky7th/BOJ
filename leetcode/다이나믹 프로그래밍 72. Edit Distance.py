# https://en.wikipedia.org/wiki/Edit_distance
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1_len, word2_len = len(word1), len(word2)
        d = [[0 for _ in range(word2_len + 1)] for _ in range(word1_len + 1)]

        for i in range(word1_len + 1):
            d[i][0] = i

        for i in range(word2_len + 1):
            d[0][i] = i

        for i in range(1, word1_len + 1):
            for j in range(1, word2_len + 1):
                if word1[i - 1] == word2[j - 1]:
                    d[i][j] = d[i - 1][j - 1]
                else:
                    d[i][j] = min([d[i - 1][j - 1], d[i - 1][j], d[i][j - 1]]) + 1

        return d[word1_len][word2_len]

solution = Solution()
print(solution.minDistance('horos', 'ros'))