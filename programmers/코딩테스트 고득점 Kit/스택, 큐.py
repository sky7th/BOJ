#프린터
# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.
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