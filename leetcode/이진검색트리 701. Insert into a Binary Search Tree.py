# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)

        self.recur(root, None, None, val)
        return root

    def recur(self, node, before_node, is_left, val):
        if node is None:
            if is_left:
                before_node.left = TreeNode(val)
            else:
                before_node.right = TreeNode(val)
            return

        if val < node.val:
            self.recur(node.left, node, True, val)
        else:
            self.recur(node.right, node, False, val)