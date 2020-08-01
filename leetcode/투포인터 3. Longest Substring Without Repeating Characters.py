class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or s is None:
            return 0
        counts = defaultdict(int)
        counts[s[0]] = 1
        start, end = 0, 0
        ret = 1
        while start < len(s) and end < len(s):
            end += 1
            if end == len(s):
                break
            counts[s[end]] += 1
            while counts[s[end]] > 1:
                counts[s[start]] -= 1
                start += 1
            ret = max(ret, end - start + 1)

        return ret