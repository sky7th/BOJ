class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ret = []
        candidates = sorted(candidates)
        self.backtrack(candidates, target, [], 0)

        return self.ret

    def backtrack(self, candidates, remain, nowCandidates, start):
        if remain < 0:
            return
        if remain == 0:
            self.ret.append(nowCandidates[:])
            return

        for i in range(start, len(candidates)):
            nowCandidates.append(candidates[i])
            self.backtrack(candidates, remain - candidates[i], nowCandidates, i)
            nowCandidates.pop()