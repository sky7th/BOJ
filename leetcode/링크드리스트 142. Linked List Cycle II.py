# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        walker = head
        runner = head

        while runner:
            runner = runner.next
            if runner:
                runner = runner.next
                walker = walker.next
                if runner is walker:
                    if runner is head:
                        return runner
                    walker = head
                    while runner is not walker:
                        runner = runner.next
                        walker = walker.next
                        if runner is walker:
                            return runner

        return None