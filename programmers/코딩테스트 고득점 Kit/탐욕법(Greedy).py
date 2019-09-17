#체육복
def solution(n, lost, reserve):
    reserveSet = set(reserve)-set(lost)
    lostSet = set(lost)-set(reserve)
    for i in reserveSet:
        if i-1 in lostSet:
            lostSet.remove(i-1)
        elif i+1 in lostSet:
            lostSet.remove(i+1)
    answer = n-len(lostSet)
    return answer

#조이스틱
def solution(name):
    name=list(name)
    nameA=["A"]*len(name)
    idx=0
    answer = 0
    while(True):
        if name == nameA:
            break
        else:
            if name[idx] != "A":
                asciiIdx = ord(name[idx])-ord("A")
                if asciiIdx <= 13:
                    answer += asciiIdx
                else:
                    answer += 26-asciiIdx
                name[idx] = nameA[idx]
            else:
                idxR=1
                idxL=1
                for i in range(1,len(name)):
                    if name[idx+i]=="A":
                        idxR+=1
                    else:
                        break
                    if name[idx-i]=="A":
                        idxL+=1
                    else:
                        break
                if idxR <= idxL:
                    answer += idxR
                    idx += idxR
                else:
                    answer += idxL
                    idx -= idxL
                    
    return answer

#큰 수 만들기
def solution(number, k):
    length = len(number)
    if length > k:
        m = 0
        for cnt in range(k):
            for idx in range(m, length-1):
                if number[idx] < number[idx+1]:
                    number = number[:idx] + number[idx+1: ]
                    length -= 1
                    if idx > 0:
                        m = idx-1
                    break
            else:
                number = number[:length-k+cnt]
                break
        return "".join(list(number))
    else:
        return "0"

#구명보트
def solution(people, limit):
    answer = 0
    people.sort()
    length = len(people)
    lightIdx = 0
    heavyIdx = length-1
    cnt = 0
    while (lightIdx <= heavyIdx):
        if people[lightIdx]+people[heavyIdx] <= limit:
            lightIdx += 1
            heavyIdx -= 1
        else:
            heavyIdx -= 1
        cnt += 1
    return cnt

#섬 연결하기
def solution(n, costs):
    costs.sort()
    connect = [costs[0][0]]
    answer = 0
    while len(connect) < n:
        min = 123456789
        idx = 0
        for i in range(len(costs)):
            if costs[i][0] in connect and costs[i][1] in connect:
                continue
            if costs[i][0] in connect or costs[i][1] in connect:
                if costs[i][2] < min:
                    min = costs[i][2]
                    idx = i
        connect.append(costs[idx][0])
        connect.append(costs[idx][1])
        connect = list(set(connect))
        costs.pop(idx)
        answer += min
                
    return answer

#단속 카메라
def solution(routes):
    answer = 1
    routes = sorted(routes)
    tmp = routes[0][1]
    for i in range(len(routes)-1):
        if tmp > routes[i][1]:
            tmp = routes[i][1]
        if tmp < routes[i+1][0]:
            answer += 1
            tmp = routes[i+1][1]
    return answer

#저울
def solution(weight):
    weight.sort()
    sum = 1
    for i in range(len(weight)):
        if sum < weight[i]:
            break
        sum += weight[i]
    return sum
