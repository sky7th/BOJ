# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ret = []
        isReverse = False
        q = deque()
        q.append(root)

        while q:
            size = len(q)
            items = []
            for i in range(size):
                cur = q.popleft()
                if cur is None:
                    continue
                items.append(cur.val)

                q.append(cur.left)
                q.append(cur.right)

            if isReverse: items = items[::-1]
            if items: ret.append(items)
            isReverse = not isReverse

        return ret

# 스택 사용한 풀이
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return None

        ret = []
        s1 = []
        s2 = []
        s1.append(root)
        isReverse = False

        while len(s1) > 0 or len(s2) > 0:
            now_s = s1 if s1 else s2
            size = len(now_s)
            items = []
            for _ in range(size):
                cur = now_s.pop()
                items.append(cur.val)
                if isReverse:
                    if cur.right is not None: s2.append(cur.right)
                    if cur.left is not None: s2.append(cur.left)
                else:
                    if cur.left is not None: s1.append(cur.left)
                    if cur.right is not None: s1.append(cur.right)

            ret.append(items)
            isReverse = not isReverse

        return ret