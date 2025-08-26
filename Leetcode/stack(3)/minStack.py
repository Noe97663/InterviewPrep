# define a stack class where all operations run in O(1) time
# include a getMin operation that tells you the minimum in the stack

## brute force - O(n) for getMin with a linear search
## 2 stack - use a 2nd stack that keeps track of the min with each
##           element added - O(1), O(n)

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]