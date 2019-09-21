#완주하지 못한 선수
# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
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
# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
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
# 스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.
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
# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 
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