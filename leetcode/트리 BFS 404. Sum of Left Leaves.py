# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # 재귀 사용 풀이
    s = 0

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root != None:
            self.recur(root, False)

        return self.s

    def recur(self, node, isLeft):
        if node == None:
            return

        if isLeft and node.left == None and node.right == None:
            self.s += node.val

        self.recur(node.left, True)
        self.recur(node.right, False)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # 큐 사용 풀이
    s = 0

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        q = deque()
        q.append(root)

        while q:
            cur = q.popleft()

            if cur is None:
                continue

            if cur.left is not None and cur.left.left is None and cur.left.right is None:
                self.s += cur.left.val
            else:
                q.append(cur.left)

            q.append(cur.right)

        return self.s
