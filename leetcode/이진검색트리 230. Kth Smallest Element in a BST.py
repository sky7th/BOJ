# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.order = 0
        self.ret = None

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.inorder(k, root)
        return self.ret.val

    def inorder(self, k, node):
        if node is None:
            return False

        if self.inorder(k, node.left):
            return True
        self.order += 1
        if self.order == k:
            self.ret = node
            return True
        return self.inorder(k, node.right)
