# def solution(k, room_numbers):
#     answer = []
#     next_rooms = list(range(k + 1))
#
#     for room_number in room_numbers:
#         a = find(next_rooms, room_number)
#         answer.append(a)
#         next_rooms[a] = find(next_rooms, a + 1)
#
#     return answer
#
#
# def find(next_rooms, n):
#     if next_rooms[n] == n:
#         return n
#
#     return find(next_rooms, n + 1)
#
#
# def union(next_rooms, n, m):
#     next_rooms[n] = next_rooms[m]


# real_rooms를 배열로 하면 효율성 4,5,6에서 런타임 에러가 뜸
import sys
sys.setrecursionlimit(10**6)


def solution(k, room_number):
    answer = []
    real_rooms = dict()

    for wanted_room in room_number:
        empty_room = find_empty_room(real_rooms, wanted_room)
        answer.append(empty_room)

    return answer


def find_empty_room(real_rooms, wanted_room):
    if wanted_room not in real_rooms:
        real_rooms[wanted_room] = wanted_room + 1
        return wanted_room

    empty_room = find_empty_room(real_rooms, real_rooms[wanted_room])
    real_rooms[wanted_room] = empty_room + 1

    return empty_room


print(solution(10, [1, 3, 4, 1, 3, 1]))
