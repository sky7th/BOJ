class Solution:
    def twoSum(self, nums, target):
        d = dict()
        for i, cur in enumerate(nums):
            if target - cur in d:
                return [d[target - cur], i]
            d[cur] = i


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
