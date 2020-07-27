class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            if len(pq) < k:
                heapq.heappush(pq, num)
            else:
                if num <= pq[0]:
                    continue
                heapq.heappop(pq)
                heapq.heappush(pq, num)

        return pq[0]
