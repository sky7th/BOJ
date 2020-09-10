class Node:
    def __init__(self, data):
        self.data = data
        self.count = 0
        self.child = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur = self.head
        cur.count += 1

        for c in string:
            if c not in cur.child:
                cur.child[c] = Node(c)
            cur = cur.child[c]
            cur.count += 1

    def count(self, prefix):
        cur = self.head

        for c in prefix:
            if c not in cur.child:
                return 0
            cur = cur.child[c]

        return cur.count


def solution(words, queries):
    answer = []

    tries = create_trie(words)
    reversed_tries = create_trie(words, True)

    for query in queries:
        answer.append(count_matched_word(tries, reversed_tries, query))

    return answer


def create_trie(words, is_reversed=False):
    trie_dic = {i: Trie() for i in range(1, 10001)}

    for word in words:
        if is_reversed:
            word = word[::-1]
        trie_dic[len(word)].insert(word)

    return trie_dic


def count_matched_word(tries, reversed_tries, query):
    no_mark_query = query.replace('?', '')

    if query[0] == '?':
        return reversed_tries[len(query)].count(no_mark_query[::-1])
    else:
        return tries[len(query)].count(no_mark_query)