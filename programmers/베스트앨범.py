def solution(genres, plays):
    genre_dic = {}
    song_dic = {}

    for song_id, (genre, play_count) in enumerate(zip(genres, plays)):
        if song_dic.get(song_id) is None:
            song_dic[song_id] = {'genre': genre, 'play_count': play_count}

        if genre_dic.get(genre) is None:
            genre_dic[genre] = {'songs': [], 'play_count': 0}

        genre_dic[genre]['play_count'] += play_count
        genre_dic[genre]['songs'].append(song_id)

    ordered_genre_dic = dict(sorted(genre_dic.items(), key=lambda x: -x[1]['play_count']))
    best_album = []

    for genre in ordered_genre_dic.keys():
        ordered_songs = sorted(ordered_genre_dic[genre]['songs'], key=lambda x: -song_dic[x]['play_count'])
        best_album.extend(ordered_songs[:2])

    return best_album


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))