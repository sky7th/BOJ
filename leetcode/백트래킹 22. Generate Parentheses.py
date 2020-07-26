class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        self.process(n, 0, 0, '', ret)
        return ret

    def process(self, n, openedCount, closedCount, s, ret):
        if openedCount == n and closedCount == n:
            ret.append(s)
            return

        if openedCount < n:
            self.process(n, openedCount + 1, closedCount, s + '(', ret)

        if openedCount > closedCount:
            self.process(n, openedCount, closedCount + 1, s + ')', ret)
