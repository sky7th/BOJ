class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        q = deque()
        visited = set()
        q.append(0)
        visited.add(0)

        while q:
            cur = q.popleft()
            for i in range(cur + 1, len(s) + 1):
                if i in visited:
                    continue
                if s[cur:i] not in wordDict:
                    continue
                if i == len(s):
                    return True
                q.append(i)
                visited.add(i)

        return False




# DP 풀이
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        b = [False for _ in range(len(s) + 1)]
        b[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if b[j] and s[j:i] in wordDict:
                    b[i] = True
                    break

        return b[len(s)]