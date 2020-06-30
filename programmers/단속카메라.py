def solution(routes):
    routes = sorted(routes)
    location = routes[0][1]
    count = 1

    for i in range(len(routes) - 1):
        if location > routes[i][1]:
            location = routes[i][1]

        if location < routes[i + 1][0]:
            location = routes[i + 1][1]
            count += 1

    return count


print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
