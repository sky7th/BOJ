class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret, n = [], len(nums)
        nums.sort()

        for i in range(n) :
            if i > 0 and nums[i] == nums[i-1] :
                continue

            l, r = i+1, n-1

            while l < r :
                s = nums[i] + nums[l] + nums[r]
                if s < 0 :
                    l += 1
                elif s > 0 :
                    r -= 1
                else :
                    ret.append([nums[l],nums[i],nums[r]])
                    while l < n-1 and nums[l] == nums[l+1] :
                        l += 1
                    while r > 1 and nums[r] == nums[r-1] :
                        r -= 1
                    l += 1
                    r -= 1

        return ret
