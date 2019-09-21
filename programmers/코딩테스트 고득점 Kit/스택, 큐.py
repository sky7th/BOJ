#프린터
from collections import deque

def solution(p, lo):
    answer = 0
    l = deque([(v,i) for i,v in enumerate(p)])
    order = 0

    while len(l) > 1:
        f = l.popleft()
        if f[0] < max(l)[0]:
            l.append(f)
        else:
            order += 1
            if f[1] == lo:
                return order
    return order + 1