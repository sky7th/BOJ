class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        rot = left
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            realMid = (mid + rot) % n
            if nums[realMid] == target:
                return realMid

            if nums[realMid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1