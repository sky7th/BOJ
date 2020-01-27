from collections import deque as queue
from collections import defaultdict

def solution(maps):
    answer = []
    couple = []
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    n = len(maps)
    m = len(maps[0])
    for i, v in enumerate(maps):  # 2차원 필드로 만들고
        maps[i] = list(v)
    for i in range(n):  # 필드를 돌면서
        for j in range(m):
            if(maps[i][j] != '.'): # 현재 위치가 나라일 경우
                name = maps[i][j] # 나라 이름을 기억해 둠
                maps[i][j] = '.'  # 지난 곳은 방문 처리를 함
                q = queue()
                q.append((i, j))
                while len(q) != 0:  # 현재 위치로 부터 동서남북으로 BFS 탐색을 시작함
                    cur = q.popleft()
                    for dir in range(4):
                        ny = cur[0] + dy[dir]
                        nx = cur[1] + dx[dir]
                        if ny<0 or ny>=n or nx<0 or nx>=m or maps[ny][nx]=='.': # 필드 밖에 나가거나 나라가 아닌 경우 예외 처리
                            continue
                        if maps[ny][nx] == name:  # 다음 위치가 현재 나라와 같은 경우 큐에 추가
                            q.append((ny,nx))
                            maps[ny][nx] = '.'
                        else: # 다음 위차가 다른 나라일 경우(국경을 공유) 
                            c = sorted((name, maps[ny][nx])) 
                            if c not in couple: # 중복되지 않게 그 쌍을 저장해놓음
                                couple.append(c)
    d = defaultdict(list) # 각 나라에서 국경을 공유하는 나라가 얼마나 있는지 알기 위해 dict 생성
    for c in couple: 
        d[c[0]].append(c[1])
    max_couple_num = 0
    for c in d: # dict 를 돌면서 국경을 공유하는 나라 개수가 가장 많은 경우를 고름
        l = len(d[c])
        if max_couple_num < l:
            max_couple_num = l
    answer.append(len(couple))
    answer.append(max_couple_num)
    
    return answer

print(solution(["..........", "AAACC.....", ".AAA.....Z", "..AAAA..C.", "...BBBBB..", "....BBB...", "...ZBBB...", "ZZZZAAAC..", ".....CCCC.", "QQ......C.", ".........."]))