class Solution:
    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits: str) -> List[str]:
        self.output = []
        if digits:
            self.backtrack("", digits)

        return self.output

    def backtrack(self, combination, next_digits):
        if len(next_digits) == 0:
            self.output.append(combination)
            return

        for letter in self.phone[next_digits[0]]:
            self.backtrack(combination + letter, next_digits[1:])