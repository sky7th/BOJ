class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        start = left
        if start == n-1 or nums[start] != target:
            return [-1, -1]

        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid

        end = left if left == n - 1 and nums[left] == target else left - 1

        return [start, end]

