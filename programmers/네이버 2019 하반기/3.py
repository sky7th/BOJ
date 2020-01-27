from collections import defaultdict

def solution(cook_times, order, k):
    d = defaultdict(list)

    for v in order:
        d[v[0]].append(v[1])

    print(d)
    
    visited = [0 for i in range(len(d))]
    print(visited)
    def dfs(order, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            for i in range(0, len(order)):
                if order[j][i] == 1 and visited[i] == 0:
                    stack.append(i)
    i=0
    res = 0
    while 0 in visited:
        if visited[i] ==0:
            dfs(d[k], visited, i)
            res += 1
        i+=1
    print(res)

    return

solution([5, 30, 15, 30, 35, 20, 4], [[2, 4], [2, 5], [3, 4], [3, 5], [1, 6], [4, 6], [5, 6], [6, 7]], 6)