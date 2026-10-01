# stack is LIFO

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack: 
            self.minStack.append(val)
        else:
            # just make sure for each step, 
            # the top one on the Stack is the smallest so far
            self.minStack.append(min(val, self.minStack[-1]))


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
