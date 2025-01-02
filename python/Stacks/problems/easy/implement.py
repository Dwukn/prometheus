class Stack:
    def __init__(self):
        """Initialize the stack."""
        self.stack = []

    def push(self, item):
        """Push an item onto the stack."""
        self.stack.append(item)

    def pop(self):
        """Pop an item from the stack."""
        if self.is_empty():
            return "Stack is empty!"
        return self.stack.pop()

    def peek(self):
        """Peek at the top item of the stack."""
        if self.is_empty():
            return "Stack is empty!"
        return self.stack[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the size of the stack."""
        return len(self.stack)

stack = Stack()
stack.push('hello')
stack.push('world')
stack.push('of')
stack.push('Stacks')
var = list(stack.stack)
print(*var)
print(stack.peek())
print(stack.pop()) # Output: 'python'
print(stack.pop()) # Output: 'world'
