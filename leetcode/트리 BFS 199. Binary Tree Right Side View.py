# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ret = []
        if root is None:
            return ret

        q = deque()
        q.append(root)

        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if i == size - 1:
                    ret.append(cur.val)

                if cur.left is not None:
                    q.append(cur.left)

                if cur.right is not None:
                    q.append(cur.right)

        return ret
