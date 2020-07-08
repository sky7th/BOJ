def solution(cookie):
    result = 0

    for i in range(len(cookie)-1):
        front_sum, front_idx = cookie[i], i
        end_sum, end_idx = cookie[i+1], i+1

        while True:
            if front_sum == end_sum:
                result = max(result, front_sum)

            if front_idx > 0 and front_sum <= end_sum:
                front_idx -= 1
                front_sum += cookie[front_idx]

            elif end_idx < len(cookie)-1 and front_sum >= end_sum:
                end_idx += 1
                end_sum += cookie[end_idx]
            else:
                break

    return result
