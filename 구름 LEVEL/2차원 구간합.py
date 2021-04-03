N = int(input())
field = []
for _ in range(N):
    field.append(list(map(int, input().split())))

x1, y1, x2, y2 = list(map(int, input().split()))
answer = 0
for i in range(y1, y2 + 1):
    for j in range(x1, x2 + 1):
        answer += field[i][j]

print(answer)
