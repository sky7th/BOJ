def solution(n, t, m, timetable):
    timetable = sorted([get_minutes(time) for time in timetable])
    START_BUS_TIME = 540
    bus_table = [START_BUS_TIME + i*t for i in range(n)]
    for bus_time in bus_table:
        passenger = [p for p in timetable if p <= bus_time]
        if bus_time == bus_table[-1]:
            if len(passenger) < m:
                return get_time(bus_time)

            return get_time(passenger[m - 1] - 1)

        if len(passenger) < m:
            timetable = timetable[len(passenger):]
        else:
            timetable = timetable[m:]


def get_minutes(time_str):
    hour, min = time_str.split(':')
    return int(hour)*60 + int(min)


def get_time(minutes):
    hour, min = str(minutes // 60), str(minutes % 60)
    return hour.zfill(2) + ':' + min.zfill(2)


print(solution(1, 1, 4, ["09:10", "09:09", "08:00"]))
