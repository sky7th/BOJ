# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.minDiff = math.inf
        self.isInit = False
        self.prev = None
        self.inorder(root)
        return self.minDiff

    def inorder(self, root):
        if root == None:
            return

        self.inorder(root.left)
        if not self.isInit:
            self.isInit = True
        else:
            self.minDiff = min(self.minDiff, root.val - self.prev)

        self.prev = root.val
        self.inorder(root.right)