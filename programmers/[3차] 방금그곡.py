def solution(m, musicinfos):
    m = convert_sharp_tone(m)
    result = []
    for index, musicinfo in enumerate(musicinfos):
        start_time, end_time, title, tones = musicinfo.split(',')
        running_time = convert_to_minutes(end_time) - convert_to_minutes(start_time)
        tones = convert_sharp_tone(tones)
        tones = make_tones_matched_running_time(tones, running_time)
        if m in tones:
            result.append({'id': index, 'running_time': running_time, 'title': title})

    if len(result) == 0:
        return '(None)'

    return sorted(result, key=lambda x: (-x['running_time'], x['id']))[0]['title']


def convert_to_minutes(time_str):
    hour, minute = time_str.split(':')
    return int(hour) * 60 + int(minute)


def convert_sharp_tone(tones):
    return tones.replace('A#', 'a').replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g')


def make_tones_matched_running_time(tones, running_time):
    mok, nam = divmod(running_time, len(tones))
    return tones * mok + tones[:nam]


print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
