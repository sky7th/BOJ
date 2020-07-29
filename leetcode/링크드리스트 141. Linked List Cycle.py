# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        walker = head
        runner = head

        while runner:
            runner = runner.next
            if runner:
                runner = runner.next
                walker = walker.next
                if runner is walker:
                    return True

        return False