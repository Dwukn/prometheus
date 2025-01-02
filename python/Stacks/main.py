class Stack:
    def __init__(self):
        self.stack = []

    # Push element onto the stack
    def push(self, item):
        self.stack.append(item)

    # Pop element from the stack
    def pop(self):
        if self.isEmpty():
            return "Stack is empty!"
        return self.stack.pop()

    # Peek the top element
    def peek(self):
        if self.isEmpty():
            return "Stack is empty!"
        return self.stack[-1]

    # Check if stack is empty
    def isEmpty(self):
        return len(self.stack) == 0

    # Get the size of the stack
    def size(self):
        return len(self.stack)


def clasMain():
    # Usage
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print("Peek: ",stack.peek())  # Output: 20
    print("Pop:",stack.pop())   # Output: 20
    print("Size:",stack.size()) # Output: 1
    x = input("Enter a number: ")
    print("pushing",stack.push(x)) # push x in stack
    print("Pop:",stack.pop())   # Output: 6
    print("isEmpty", stack.isEmpty())  # Output: 1
    print("Pop:",stack.pop())   # Output: 10
    print("isEmpty", stack.isEmpty())  # Output: 1

def is_balanced(expression):
    stack = Stack()

    for char in expression:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.isEmpty():
                return False
            stack.pop()

    return stack.isEmpty()

def balancingmain():
    # Usage
    print(f'checking if (a+b) is balanced {is_balanced("(a+b)")}')  # True
    print(f'checking if ((a+b) is balanced {is_balanced("((a+b)")}')  # False


if __name__ == "__main__":
    # clasMain()
    balancingmain()
