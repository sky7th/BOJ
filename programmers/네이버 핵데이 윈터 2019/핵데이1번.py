def solution(grade):
    answer = 0
    min_grade = min(grade)
    min_index = grade.index(min_grade) # 가장 작은 수를 찾고
    for i in range(min_index, 0, -1): # 그 수를 기준으로 앞으로 for문을 돌면서 
        if grade[i-1] > grade[i]: # 앞에 있는 수가 클 경우 현재 값으로 바꿔줌 (현재 값과 같게 해야 최소값을 구할 수 있음)
            answer += (grade[i-1] - grade[i])
            grade[i-1] = grade[i]
    for i in range(min_index+1, len(grade), 1): # 그 수를 기준으로 뒤로 for문을 돌면서
        if grade[i-1] > grade[i]: # 앞에 있는 수가 클 경우 현재 값으로 바꿔줌
            answer += (grade[i-1] - grade[i])
            grade[i-1] = grade[i]

    return answer

print(solution([2,1,3]))