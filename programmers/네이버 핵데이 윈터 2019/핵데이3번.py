def solution(command, buttons, scores):
    max_score = len(command); # 초기값은 스킬 사용안하고 기본 점수일 떄
    while buttons:  # 모든 경우의 수를 보기 위함
        com = command
        sum_score = 0;
        for i, button in enumerate(buttons):
            if button in com:
                sum_score += scores[i]
                com = com.replace(button, '') # 해당 스킬을 시용했으면 커맨드에서 없애줌
            v = sum_score+len(com)  # 나머지 남은 버튼들의 점수가 스킬을 썼을 때보다 점수가 높을 수도 있으므로,
            if max_score < v:       # 스킬을 사용할 때마다 나머지 버튼들의 점수(1점)을 더해서 max 값과 비교
                max_score = v
        buttons.pop(0)
        scores.pop(0)
        
    return max_score

print(solution("<v>AB^CYv^XAZ", ["v>AB^CYv^XA", "<v>A", "^XAZ", "Yv^XA", ">AB^"], [50, 18, 20, 30, 25]))