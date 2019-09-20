#완주하지 못한 선수
def solution(s,c):
    s.sort()
    c.sort()
    for par, com in zip(s, c) :
        if par != com :
            return par
    return s[-1]
#best
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


#전화번호 목록
def solution(pb):
    answer = True
    pb.sort()
    for i in range(len(pb)-1):
        if pb[i] in pb[i+1]:
            answer = False
                
    return answer
#정규표현식 풀이
import re
def solution(phoneBook):

    for b in phoneBook:
        p = re.compile("^"+b)
        for b2 in phoneBook:
            if b != b2 and p.match(b2):
                return False
    return True


#위장
from collections import Counter

def solution(clothes):
    answer = 1
    clothe_cnt = Counter([c for _, c in clothes])
    for c in clothe_cnt:
        answer *= (clothe_cnt[c]+1)  
    return answer-1
#reduce 사용
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer


#베스트 앨범
from collections import defaultdict

def solution(genres, plays):
    play_count_by_genre = defaultdict(int)
    songs_in_genre = defaultdict(list)
    song_id = 0

    for genre, play in zip(genres, plays):
        play_count_by_genre[genre] -= play
        songs_in_genre[genre].append((-play, song_id))
        song_id += 0

    genre_in_order = sorted(play_count_by_genre.keys(), key=lambda g:play_count_by_genre[g])
    answer = list()

    for genre in genre_in_order:
        print(genre)
        answer.extend([ song_id for minus_play, song_id in sorted(songs_in_genre[genre])[:2]])
    return answer