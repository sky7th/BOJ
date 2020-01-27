m, n = map(int, input().strip().split(' '))
y, x = map(int, input().strip().split(' '))

if y > n or y < 0 or x > m or x < 0:
    print('fail')

field = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(m+1):
    field[0][i] = 1
for i in range(n+1):
    field[i][0] = 1

for i in range(1, n+1):
    for j in range(1, m+1):
        field[i][j] = field[i-1][j] + field[i][j-1]
        if (i, j) == (y, x):
            print(y + x)
            print(field[i][j])
