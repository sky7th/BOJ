## DP 시간초과
class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = [math.inf for _ in nums]
        memo[-1] = 0
        lastPos = len(nums) - 1

        for i in range(lastPos - 1, -1, -1):
            minn = math.inf
            for j in range(i + 1, i + nums[i] + 1):
                if j > lastPos:
                    break

                if memo[j] == math.inf:
                    continue

                minn = min(minn, memo[j])

            memo[i] = minn + 1

        return memo[0]
    
    
# bfs 시간초과
class Solution:
    def jump(self, nums: List[int]) -> int:
        visited = [False for _ in nums]
        q = deque()
        q.append(0)
        visited[0] = True
        depth = 0

        while q:
            size = len(q)
            for _ in range(size):
                idx = q.popleft()

                if idx == len(nums) - 1:
                    return depth

                for i in range(1, nums[idx] + 1):
                    nextIdx = idx + i
                    if nextIdx > len(nums) - 1:
                        break

                    if visited[nextIdx]:
                        continue

                    q.append(nextIdx)
                    visited[nextIdx] = True

            depth += 1

        return -1


# 갓갓 솔루션
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        step, max_range, next_range = 1, nums[0], nums[0]

        for i in range(1, len(nums)):
            if max_range >= len(nums) - 1:
                return step

            if i > max_range:
                max_range = next_range
                step += 1

            next_range = max(next_range, i + nums[i])

        return step