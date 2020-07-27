class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = [[0, 0] for _ in range(len(nums))]
        d[0][0] = nums[0]
        d[0][1] = nums[0]

        for i, num in enumerate(nums):
            if i == 0: continue

            d[i][0] = min([num, num * d[i - 1][0], num * d[i - 1][1]])
            d[i][1] = max([num, num * d[i - 1][0], num * d[i - 1][1]])

        res = d[0][1]
        for i in range(len(d)):
            res = max(res, d[i][1])

        return res
