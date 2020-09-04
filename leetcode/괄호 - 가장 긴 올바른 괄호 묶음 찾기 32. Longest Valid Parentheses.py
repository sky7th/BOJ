# 스택 사용하는 방법
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = []
        stack.append(-1)

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])

        return res



# 신박한 방법
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = maxLen = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                maxLen = max(maxLen, 2 * right)

            if left < right:
                left = right = 0

        left = right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                maxLen = max(maxLen, 2 * left)

            if left > right:
                left = right = 0

        return maxLen


