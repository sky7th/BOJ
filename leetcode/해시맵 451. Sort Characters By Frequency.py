class Solution:
    def frequencySort(self, s: str) -> str:
        answer = ''
        for k, v in Counter(s).most_common():
            for _ in range(v):
                answer += k

        return answer
