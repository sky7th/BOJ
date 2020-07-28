class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        indegrees = [0 for _ in range(numCourses)]

        for a, b in prerequisites:
            g[a].append(b)
            indegrees[b] += 1

        q = deque()
        for node in range(numCourses):
            if indegrees[node] == 0:
                q.append(node)

        ret = []
        while q:
            cur = q.popleft()
            ret.append(cur)
            for nxt_node in g[cur]:
                indegrees[nxt_node] -= 1
                if indegrees[nxt_node] == 0:
                    q.append(nxt_node)

        return ret[::-1] if len(ret) == numCourses else []