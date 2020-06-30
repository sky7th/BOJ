from math import ceil


def solution(n, stations, w):
    answer = 0
    no_zone_distances = [stations[0] - w - 1, n - (stations[-1] + w)]

    for i in range(1, len(stations)):
        dist = (stations[i] - w - 1) - (stations[i - 1] + w)
        if dist > 0:
            no_zone_distances.append((stations[i] - w - 1) - (stations[i - 1] + w))

    for dist in no_zone_distances:
        answer += ceil(dist / (w * 2 + 1))

    return answer