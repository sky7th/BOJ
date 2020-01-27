def solution(n):
    D = [0 for _ in range(10000001)]
    store = [2]

    D[0] = 0
    D[1] = 1

    count = 2
    while True:
        D[count] = D[count-1] * count
        for i in range(1, count-1):
            store.append(D[count] // D[i])
            if len(store) == n*10:
                list(set(store))
                store.sort()
                return store[n-1]
        count += 1

print(solution(4))