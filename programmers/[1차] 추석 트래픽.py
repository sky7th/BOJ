def solution(lines):
    times = list(map(make_processing_start_end_time, lines))

    return get_maximum_throughput_per_second(times)

def make_processing_start_end_time(line):
    _, date, processing_time = line.split()
    processing_time_ms = int(float(processing_time[0:-1]) * 1000)
    end_time_ms = make_milliseconds(date)
    start_time_ms = end_time_ms - processing_time_ms + 1

    return start_time_ms, end_time_ms

def make_milliseconds(date):
    h, m, s = date.split(':')
    s, ms = s.split('.')

    return (int(h) * 3600 + int(m) * 60 + int(s)) * 1000 + int(ms)

def get_maximum_throughput_per_second(times):
    max_count = 0
    for time in times:
        _, end_time_ms = time
        count = count_within_range(times, end_time_ms, end_time_ms + 999)
        max_count = max(max_count, count)

    return max_count

def count_within_range(times, start_of_range, end_of_range):
    count = 0
    for time in times:
        start_time_ms, end_time_ms = time
        if start_time_ms > end_of_range or end_time_ms < start_of_range:
            continue
        
        count += 1

    return count


print(solution(	["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))

