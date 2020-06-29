from math import ceil


def solution(progresses, speeds):
    days = [ceil((100 - a) / b) for a, b in zip(progresses, speeds)]
    front = -1
    counts = []

    for day in days:
        if day > front:
            counts.append(1)
            front = day
            continue

        counts[-1] += 1

    return counts