class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        d = [0 for _ in range(len(nums))]
        d[0] = 1

        for i in range(len(nums)):
            mx = 0
            for j in range(i):
                if nums[j] < nums[i] and d[j] > mx:
                    mx = d[j]

            d[i] = mx + 1

        return max(d)