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


class ExpressionEvaluator:
    def __init__(self):
        """Initialize the evaluator with a stack for operator precedence."""
        self.stack = Stack()

    def precedence(self, op):
        """Return the precedence of operators."""
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

    def infix_to_postfix(self, expression):
        """Convert an infix expression to postfix notation."""
        postfix = []
        for char in expression:
            if char.isalpha():  # Operand (e.g., letter or number)
                postfix.append(char)
            elif char == '(':  # Left Parenthesis
                self.stack.push(char)
            elif char == ')':  # Right Parenthesis
                while not self.stack.is_empty() and self.stack.peek() != '(':
                    postfix.append(self.stack.pop())
                self.stack.pop()  # Remove '('
            else:  # Operator
                while (not self.stack.is_empty() and
                       self.precedence(self.stack.peek()) >= self.precedence(char)):
                    postfix.append(self.stack.pop())
                self.stack.push(char)

        # Pop any remaining operators from the stack
        while not self.stack.is_empty():
            postfix.append(self.stack.pop())

        return ''.join(postfix)

    def is_balanced(self, expression):
        """Check if parentheses in the expression are balanced."""
        temp_stack = Stack()  # Use a temporary stack for balancing
        matching_brackets = {')': '(', '}': '{', ']': '['}

        for char in expression:
            if char in "({[":
                temp_stack.push(char)
            elif char in ")}]":
                if temp_stack.is_empty() or temp_stack.pop() != matching_brackets[char]:
                    return False
        return temp_stack.is_empty()  # If the stack is empty, parentheses are balanced


def main():
    evaluator = ExpressionEvaluator()

    # Example of balanced parentheses checking
    print(f'Checking if "{'(a+b)'}" is balanced: {evaluator.is_balanced("{[()()]}")}')  # True
    print(f'Checking if "{'(a+b'}" is balanced: {evaluator.is_balanced("((a+b)")}')  # False

    # Example of infix to postfix conversion
    infix_expr_1 = "(a+b)*c-(d/e)"
    print(f'Infix expression: {infix_expr_1}')
    print(f'Postfix expression: {evaluator.infix_to_postfix(infix_expr_1)}')

    infix_expr_2 = "a+b*(c^d-e)^(f+g*h)-i"
    print(f'Infix expression: {infix_expr_2}')
    print(f'Postfix expression: {evaluator.infix_to_postfix(infix_expr_2)}')


if __name__ == "__main__":
    main()
