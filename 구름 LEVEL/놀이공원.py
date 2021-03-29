T = int(input())
N, K = map(int, input().split())
field = []
for _ in range(N):
    raw = list(map(int, input().split()))
    field.append(raw)

answer = N**2
for i in range(N - K + 1):
    for j in range(N - K + 1):
        count = 0
        for n in range(i, i + K):
            for m in range(j, j + K):
                if field[n][m] == 1:
                    count += 1

        answer = min(answer, count)

print(answer)
