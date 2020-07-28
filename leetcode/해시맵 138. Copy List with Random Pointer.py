"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        cur = head
        d = dict()
        d[cur] = Node(cur.val, cur.next, cur.random)

        while cur:
            d[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            if cur.next is None:
                d[cur].next = None
            else:
                d[cur].next = d[cur.next]

            if cur.random is None:
                d[cur].random = None
            else:
                d[cur].random = d[cur.random]

            cur = cur.next

        return d[head]


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        cur = head
        d = dict()
        d[cur] = Node(cur.val, cur.next, cur.random)

        while cur:
            d[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            if cur.next is None:
                d[cur].next = None
            else:
                d[cur].next = d[cur.next]

            if cur.random is None:
                d[cur].random = None
            else:
                d[cur].random = d[cur.random]

            cur = cur.next

        return d[head]

# 1번만 순회하는 풀이
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        d = dict()
        ret = Node(head.val)
        cur = ret
        d[head] = cur

        while head:
            if head.next is not None:
                if head.next not in d:
                    d[head.next] = Node(head.next.val)
                cur.next = d[head.next]

            if head.random is not None:
                if head.random not in d:
                    d[head.random] = Node(head.random.val)
                cur.random = d[head.random]

            head = head.next
            cur = cur.next

        return ret
