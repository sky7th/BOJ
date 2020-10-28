class Solution(object):
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, start, path, res):
        res.append(path)
        for i in range(start, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)

    def subsets(self, nums):
        ret = []
        self.dfs(nums, [], ret)
        return ret

    def dfs(self, nums, path, ret):
        ret.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i + 1:], path + [nums[i]], ret)

    # Bit Manipulation
    def subsets(self, nums):
        res = []
        nums.sort()
        for i in range(1 << len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res

    # Iteratively
    def subsets(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item + [num] for item in res]
        return res