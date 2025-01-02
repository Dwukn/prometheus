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


class Usage:
    def __init__(self):
        self.stack = Stack()  # Using Stack class

    # Wrapper methods for stack operations
    def push(self, item):
        self.stack.push(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack.peek()

    def isEmpty(self):
        return self.stack.isEmpty()

    def size(self):
        return self.stack.size()

    # Define precedence of operators
    def precedence(self, op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return 0

    # Convert infix to postfix notation
    def infix_to_postfix(self, expression):
        postfix = []
        for char in expression:
            if char.isalpha():  # Operand (letter or number)
                postfix.append(char)
            elif char == '(':  # Left Parenthesis
                self.stack.push(char)
            elif char == ')':  # Right Parenthesis
                while not self.stack.isEmpty() and self.stack.peek() != '(':
                    postfix.append(self.stack.pop())
                self.stack.pop()  # Remove '('
            else:  # Operator
                while (not self.stack.isEmpty() and
                       self.precedence(self.stack.peek()) >= self.precedence(char)):
                    postfix.append(self.stack.pop())
                self.stack.push(char)

        while not self.stack.isEmpty():
            postfix.append(self.stack.pop())

        return ''.join(postfix)

    # Check if parentheses are balanced
    def is_balanced(self, expression):
        stack = []
        for char in expression:
            if char in "({[":
                stack.append(char)
            elif char in ")}]":
                if not stack:
                    return False
                top = stack.pop()
                if char == ")" and top != "(":
                    return False
                if char == "}" and top != "{":
                    return False
                if char == "]" and top != "[":
                    return False
        return not stack  # If stack is empty, it's balanced


def main():
    usage = Usage()

    # Example Usage:
    # expression =
    # print(usage.is_balanced(expression))  # Output: True

    # Usage of balancing parentheses
    print(f'Checking if (a+b) is balanced: {usage.is_balanced("{[()()]}")}')  # True
    print(f'Checking if ((a+b) is balanced: {usage.is_balanced("((a+b)")}')  # False

    # Usage of infix to postfix conversion
    expression = "(a+b)*c-(d/e)"
    print(f'Infix expression: {expression}')
    print(f'Postfix expression: {usage.infix_to_postfix(expression)}')
    expression = "a+b*(c^d-e)^(f+g*h)-i"
    print(f'Infix expression: {expression}')
    print(f'Postfix expression: {usage.infix_to_postfix(expression)}')


if __name__ == "__main__":
    main()
