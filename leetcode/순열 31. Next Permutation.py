# 주어진 nums를 수정하지 않고 배열 요소만 변경해서 푸는 문제여서 특이했다.
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        a = len(nums) - 2
        while a >= 0 and nums[a] >= nums[a + 1]:
            a -= 1

        if a != -1:
            b = len(nums) - 1
            while nums[b] <= nums[a]:
                b -= 1

            self.swap(nums, a, b)

        start = a + 1
        end = len(nums) - 1
        while start < end:
            self.swap(nums, start, end)
            start += 1
            end -= 1

    def swap(self, nums, a, b):
        tmp = nums[a]
        nums[a] = nums[b]
        nums[b] = tmp
