standard_input = [
    '4',
'0 1 2 3',
'4 0 5 6',
'7 1 0 2',
'3 4 5 0'
]

N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
visited = [0 for _ in range(N)]
answer = float('inf')

def back_track(idx, count):
    if count == N // 2:
        update_stat_difference()

    for i in range(idx, N):
        if visited[i]: 
            continue

        visited[i] = 1
        back_track(i + 1, count + 1)
        visited[i] = 0
        
def update_stat_difference():
    global answer
    start_stat, link_stat = 0, 0
    for i in range(N):
        for j in range(N):
            if visited[i] and visited[j]:
                start_stat += field[i][j]

            if not visited[i] and not visited[j]:
                link_stat += field[i][j]

    answer = min(answer, abs(start_stat - link_stat))

back_track(0, 0)
print(answer)