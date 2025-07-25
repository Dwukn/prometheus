class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        # print(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
            print("value pushed in minStack: ",self.min_stack)

    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
stack = MinStack()
stack.push(0)
stack.push(0)
stack.push(1)
stack.push(9)
stack.push(10)
stack.push(7)
stack.getMin() # return -3
var = list(stack.stack)
print("Stack: ",*var)
print("Min: ",stack.getMin())
