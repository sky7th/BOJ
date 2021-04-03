N = input()
dists = list(map(int, input().split()))
p = 0
before = 0
for i in range(len(dists)):
    p = max(dists[i] - before + i, p)
    before = dists[i]

print(p)
