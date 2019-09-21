#가장 먼 노드
# n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다.
# 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다.
def solution(n, edge):
    g = [[] for _ in range(n)]
    dist = [0 for _ in range(n)]
    visited = [False for _ in range(n)]
    q = [0, 0]
    visited[0] = True
    for (a,b) in edge:
        g[a-1].append(b-1)
        g[b-1].append(a-1)

    while q:
        f = q.pop(0)
        for i in g[f]:
            if visited[i] == False:
                visited[i] = True
                q.append(i)
                dist[i] = dist[f]+1
    dist.sort(reverse=True)

    return dist.count(dist[0])


#순위
check = []

def search(direction, node):
    global check
    result = 0
    for e in direction[node-1]:
        if e not in check:
            check.append(e)
            result += search(direction, e) + 1
    return result

def solution(n, results):
    global check
    right = []
    reverse = []
    answer = 0
    for i in range(n):
        right.append([])
        reverse.append([])
    for e in results:
        right[e[0]-1].append(e[1])
        reverse[e[1]-1].append(e[0])
    for j in range(1,n+1):
        total = 0
        check = []
        total += (search(right,j) + search(reverse,j))
        if total == n-1:
            answer += 1
    return answer