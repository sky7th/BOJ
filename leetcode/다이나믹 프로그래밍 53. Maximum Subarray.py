class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = [0 for _ in range(len(nums))]
        d[0] = nums[0]

        for i in range(1, len(nums)):
            d[i] = max(d[i - 1] + nums[i], nums[i])

        return max(d)