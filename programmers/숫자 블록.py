# 효율성 시간 초과가 아닌 실패가 뜸
# 테스트 케이스가 문제 조건과 맞지 않는 것일 수도 있음
from math import sqrt


def solution(begin, end):
    result = [1 for _ in range(end - begin + 1)]
    if begin == 1:
        result[0] = 0

    for i in range(begin, end + 1):
        for j in range(2, int(sqrt(end) + 1)):
            if i % j == 0:
                result[i-begin] = i // j
                break

    return result


print(solution(999999999 , 1000000000))