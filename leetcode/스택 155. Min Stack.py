class MinStack:
    class Node:
        def __init__(self, val, min_val):
            self.val = val
            self.min_val = min_val

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        min_val = min(x, self.getMin())
        self.stack.append(self.Node(x, min_val))

    def pop(self) -> None:
        return self.stack.pop().val

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.stack[-1].min_val if self.stack else math.inf

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()