from copy import deepcopy
import re

answer = []
banned_id_matches = []


def solution(user_ids, banned_ids):
    global answer, banned_id_matches

    set_banned_id_matches(user_ids, banned_ids)
    search(set(), 0)
    return len(answer)


def set_banned_id_matches(user_ids, banned_ids):
    for i in range(len(banned_ids)):
        p = re.compile("^" + banned_ids[i].replace("*", ".") + "$")
        banned_id_matches.append({user for user in user_ids if p.match(user)})


def search(visited, idx):
    if idx == len(banned_id_matches):
        if visited not in answer:
            answer.append(deepcopy(visited))
        return

    for user in banned_id_matches[idx]:
        if user in visited:
            continue

        visited.add(user)
        search(visited, idx + 1)
        visited.remove(user)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))


# product를 사용한 풀이
from itertools import product

def check(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] == "*":
            continue
        if str1[i] != str2[i]:
            return False
    return True

def solution(user_id, banned_id):
    answer = set()
    result = [[] for i in range(len(banned_id))]

    for i in range(len(banned_id)):
        for u in user_id:
            if check(banned_id[i], u):
                result[i].append(u)

    result = list(product(*result))
    for r in result:
        if len(set(r)) == len(banned_id):
            answer.add("".join(sorted(set(r))))

    return len(answer)