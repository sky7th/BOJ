class Solution:
    def longestPalindrome(self, s: str) -> int:
        remember = set()
        for c in s:
            if c in remember:
                remember.remove(c)
            else:
                remember.add(c)

        if len(remember) in [0, 1]:
            return len(s)
        else:
            return len(s) - len(remember) + 1
