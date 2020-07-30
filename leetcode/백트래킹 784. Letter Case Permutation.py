class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ret = []
        self.backtrack(S, ret, 0)
        return ret

    def backtrack(self, S, ret, idx):
        if idx == len(S):
            ret.append(S)
            return

        if S[idx].isdigit():
            self.backtrack(S, ret, idx + 1)
        else:
            self.backtrack(S, ret, idx + 1)
            before_S = S
            S = S[:idx] + S[idx].swapcase() + S[idx + 1:]
            self.backtrack(S, ret, idx + 1)
            S = before_S