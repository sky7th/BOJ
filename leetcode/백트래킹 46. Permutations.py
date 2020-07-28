class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ret = []
        self.nums = nums
        tmp = []
        self.backtrack(tmp)
        return self.ret

    def backtrack(self, tmp):
        if len(tmp) == len(self.nums):
            self.ret.append(tmp[:])
            return

        for num in self.nums:
            if num in tmp:
                continue
            tmp.append(num)
            self.backtrack(tmp)
            tmp.pop()