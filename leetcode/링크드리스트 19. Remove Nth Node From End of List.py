# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0

        dummy = ListNode(0)
        dummy.next = head

        cur = head

        while cur != None:
            length += 1
            cur = cur.next

        length -= n
        cur = dummy

        while length > 0:
            cur = cur.next
            length -= 1

        cur.next = cur.next.next

        return dummy.next