# 백트래킹: 시간초과
# 시간복잡도: 2^n
# 공간복잡도: n
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.backtrack(nums, 0)

    def backtrack(self, nums, position):
        if position == len(nums) - 1:
            return True

        furthestJump = min(position + nums[position], len(nums) - 1)
        for i in range(furthestJump, position, -1):
            if self.backtrack(nums, i):
                return True

        return False


# DP 풀이 (Top-Down)
# 시간복잡도: n^2
# 공간복잡도: 2n
class Solution:
    UNKNOWN = 0
    GOOD = 1
    BAD = 2
    dp = []

    def canJump(self, nums: List[int]) -> bool:
        self.dp = [self.UNKNOWN for _ in nums]
        return self.backtrack(nums, 0)

    def backtrack(self, nums, position):
        if position == len(nums) - 1:
            return True

        if self.dp[position] == self.GOOD:
            return True

        if self.dp[position] == self.BAD:
            return False

        furthestJump = min(position + nums[position], len(nums) - 1)
        for i in range(furthestJump, position, -1):
            if self.backtrack(nums, i):
                self.dp[position] = self.GOOD
                return True

        self.dp[position] = self.BAD

        return False


# DP 풀이 (Bottom-Up)
# 시간복잡도: n^2
# 공간복잡도: n
class Solution:
    UNKNOWN = 0
    GOOD = 1
    BAD = 2
    dp = []

    def canJump(self, nums: List[int]) -> bool:
        self.dp = [self.UNKNOWN for _ in nums]
        self.dp[len(self.dp) - 1] = self.GOOD

        for i in range(len(nums) - 2, -1, -1):
            furthestJump = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, furthestJump + 1):
                if self.dp[j] == self.GOOD:
                    self.dp[i] = self.GOOD
                    break

        return self.dp[0] == self.GOOD



## 그리디 풀이
# 시간복잡도: n
# 공간복잡도: 1
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastPos = len(nums) - 1
        for i in range(lastPos, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i

        return lastPos == 0
