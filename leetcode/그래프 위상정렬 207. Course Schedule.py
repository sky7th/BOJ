class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        indegrees = [0 for _ in range(numCourses)]
        visited = [False for _ in range(numCourses)]

        for a, b in prerequisites:
            g[a].append(b)
            indegrees[b] += 1

        q = deque()
        for node in range(numCourses):
            if indegrees[node] == 0:
                q.append(node)
                visited[node] = True

        while q:
            cur = q.popleft()
            for nxt_node in g[cur]:
                indegrees[nxt_node] -= 1
                if indegrees[nxt_node] == 0:
                    q.append(nxt_node)
                    visited[nxt_node] = True

        return False if False in visited else True
