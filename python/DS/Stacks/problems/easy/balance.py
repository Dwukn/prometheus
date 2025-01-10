class Stack():
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def is_empty(self):
        return len(self.stack) == 0
    def pop(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.stack[-1]
    def size(self):
        return len(self.stack)

def balance(expression: str) ->bool:
    temp_stack = Stack()
    match = {')': '(', '}': '{', ']': '[', '>': '<'}
    if len(expression) == 0:
        print("Expression is empty")
        exit()
    else:
        for char in expression:
            #if character is an opening bracket
            if char in match.values():
            # if char in "({[":
                temp_stack.push(char)
            #if character is a closing bracket
            if char in match.keys():
            # elif char in ")}]":
                if temp_stack.is_empty() or temp_stack.pop() != match[char]:
                    return False
        return temp_stack.is_empty()

def main():
    expression = input("Enter the expression: ")
    print("Expression is : " + ('balanced' if balance(expression) else 'unbalanced'))


main()
