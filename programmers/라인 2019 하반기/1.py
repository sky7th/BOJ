from collections import deque as queue

a, b = map(int, input().strip().split(' '))
messages = queue()
working = [[False, 0] for _ in range(b)]
print(working)

for i in range(a):
    m = input()
    messages.append(int(m))
time = 0

while messages:
    for i in range(len(working)):
        if working[i][0] == False:
            working[i][1] += messages.popleft()
            working[i][0] = True
            print(working[i][1], 'aa', i)
        if working[i][1] == time:
            working[i][0] = False
    time += 1

print(max([w[1] for w in working]))