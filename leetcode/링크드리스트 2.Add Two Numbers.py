# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        self.num1 = deque()
        self.num2 = deque()

        cur = l1
        while cur:
            self.num1.appendleft(str(cur.val))
            cur = cur.next

        cur = l2
        while cur:
            self.num2.appendleft(str(cur.val))
            cur = cur.next

        ret_str = str(int(''.join(self.num1)) + int(''.join(self.num2)))
        ret = None
        cur = None
        for c in ret_str[::-1]:
            if ret is None:
                ret = ListNode(int(c))
                cur = ret
            else:
                cur.next = ListNode(int(c))
                cur = cur.next

        return ret