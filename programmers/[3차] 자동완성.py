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


def solution(words):
    trie = Trie()
    for word in words:
        trie.insert(word)

    count = 0
    for word in words:
        for idx, c in enumerate(word):
            part_of_word = word[0:idx+1]
            if trie.count(part_of_word) == 1 or part_of_word == word:
                count += len(part_of_word)
                break

    return count


print(solution(["word", "war", "warrior", "world"]))
