class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [1] + [0] * len(s)
        self.wordDict = set(wordDict)

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in self.wordDict:
                    dp[i] = 1

        self.ret = []
        if dp[-1] == 0:
            return self.ret

        self.backtrack(s, "")

        return self.ret

    def backtrack(self, s, path):
        if len(s) == 0:
            self.ret.append(path[:-1])
        for i in range(1, len(s) + 1):
            if s[:i] in self.wordDict:
                self.backtrack(s[i:], path + s[:i] + ' ')