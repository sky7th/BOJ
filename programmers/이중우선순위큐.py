import heapq


def solution(operations):
    pq = []

    for operate in operations:
        op, num = operate.split(" ")
        num = int(num)

        if op == 'D' and not pq:
            continue

        if op == 'I':
            heapq.heappush(pq, num)
        elif num == -1:
            heapq.heappop(pq)
        else:
            pq.pop()

    return [max(pq), min(pq)] if pq else [0, 0]

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
