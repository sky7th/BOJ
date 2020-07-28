# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    ret = True

    def isValidBST(self, root: TreeNode) -> bool:
        self.isValid(root)

        return self.ret

    def isValid(self, node):
        if node == None:
            return

        self.isValid(node.left)
        if self.prev != None and self.prev >= node.val:
            self.ret = False
            return
        self.prev = node.val
        self.isValid(node.right)

# 다른 풀이
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf')), ]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True


solution = Solution()

node1 = TreeNode(1)
node2 = TreeNode(1)
node1.left = node2

print(solution.isValidBST(node1))
