def solution(lines):
    times = list(map(makeProcessingStartEndTime, lines))

    return get_maximum_throughput_per_second(times)


def get_maximum_throughput_per_second(times):
    ONE_SECOND = 1000
    max_count = 0
    for time in times:
        _, end_time = time
        count = countWithinRange(times, end_time, end_time + ONE_SECOND)
        max_count = max(max_count, count)

    return max_count


def countWithinRange(times, start_of_range, end_of_range):
    count = 0
    for time in times:
        start_time, end_time = time
        if end_time < start_of_range or end_of_range < start_time:
            continue
        count += 1

    return count


def makeProcessingStartEndTime(line):
    _, date, processing_time = line.split()
    processing_time_ms = int(float(processing_time[0:-1]) * 1000)
    print(processing_time_ms)
    end_time_ms = makeMilliseconds(date)
    start_time_ms = end_time_ms - processing_time_ms + 1

    return start_time_ms, end_time_ms


def makeMilliseconds(date):
    h, m, s = date.split(':')
    s, ms = s.split('.')

    return (int(h) * 3600 + int(m) * 60 + int(s)) * 1000 + int(ms)


print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))

