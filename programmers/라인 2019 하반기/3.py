N = int(input())
times = list()
bathrooms = [0]

for i in range(N):
    a, b = map(int, input().strip().split(' '))
    times.append((a, b))
times.sort()

for i in range(N):
    for j in range(len(bathrooms)):
        if bathrooms[j] > times[i][0]:
            bathrooms.append(times[i][1])
        else:
            bathrooms[j] = times[i][1]
    
print(len(bathrooms))