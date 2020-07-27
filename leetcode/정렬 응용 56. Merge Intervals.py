class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) <= 1:
            return intervals

        intervals = sorted(intervals, key=lambda x: x[0])
        ret = []

        for i in range(1, len(intervals)):
            a = intervals[i - 1]
            b = intervals[i]

            if b[0] <= a[1]:
                b[0] = a[0]
                b[1] = max(a[1], b[1])
            else:
                ret.append(a)

        ret.append(intervals[-1])

        return ret


solution = Solution()
solution.merge([[1,4],[2,3]])