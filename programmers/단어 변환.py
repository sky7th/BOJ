from collections import deque
from collections import defaultdict


def solution(begin, target, words):
    word_dict = defaultdict(list)
    word_dict[begin].extend(list(filter(lambda x: can_convert(x, begin), words)))

    for word in words:
        word_dict[word].extend(list(filter(lambda x: can_convert(x, word), words)))

    q = deque()
    q.append((begin, 0))

    while q:
        now_word, count = q.popleft()

        if now_word == target:
            return count

        if count > len(words):
            break

        for next_word in word_dict[now_word]:
            q.append((next_word, count + 1))

    return 0


def can_convert(word1, word2):
    return list([c1 == c2 for c1, c2 in zip(word1, word2)]).count(False) == 1


print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
