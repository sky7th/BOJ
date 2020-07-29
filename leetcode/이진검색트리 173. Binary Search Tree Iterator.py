# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root is not None:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        if node.right is not None:
            cur = node.right
            while cur is not None:
                self.stack.append(cur)
                cur = cur.left

        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) != 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()