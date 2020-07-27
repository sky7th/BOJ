# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None

        pq = []
        for node in lists:
            while node is not None:
                heapq.heappush(pq, node.val)
                node = node.next

        ret = None
        tail = None
        while pq:
            if ret is None:
                ret = ListNode(heapq.heappop(pq))
                tail = ret
            else:
                tail.next = ListNode(heapq.heappop(pq))
                tail = tail.next

        return ret
