#모의고사
#best
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result


#소수 찾기
# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 
# 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
from itertools import permutations

def isPrime(a):
    if(a<2):
        return False
    for i in range(2,a):
        if(a%i==0):
            return False
    return True

def solution(numbers):
    answer = set()
    for i in range(1,len(numbers)+1):
        perm = permutations(list(numbers), i)
        for p in perm:
            num = int("".join(p))
            if isPrime(num):
                answer.add(num)
    return len(answer)


#숫자 야구
# 질문한 세 자리의 수, 스트라이크의 수, 볼의 수를 담은 2차원 배열 baseball이 매개변수로 주어질 때, 
# 가능한 답의 개수를 return 하도록 solution 함수를 작성해주세요.
#best
def st_B(given, chosen):
    st = 0
    B = 0
    chosen_dif = []
    given_dif = []
    for i in range(3):
        if given[i] == chosen[i]:
            st += 1
        else:
            given_dif.append(given[i])
            chosen_dif.append(chosen[i])
    for num in chosen_dif:
        if num in given_dif:
            B += 1
    return st, B

import itertools

def solution(baseball):
    first = list(itertools.permutations([1,2,3,4,5,6,7,8,9], 3))
    second = []
    for each in baseball:
        given = [int(i) for i in str(each[0])]
        stb = (each[1], each[2])
        for chosen in first:
            if st_B(given, chosen) == stb:
                second.append(chosen)
        first = second
        second = []
    return len(first)