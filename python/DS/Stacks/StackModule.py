from collections import deque

# Assigning the deque class to the variable 'stack'
stack = deque()

# Correctly creating a deque with the string 'test' and additional characters 'a', 'b', and 'c'
# This can be done by combining them into one iterable (like a string or a list).
a = deque('test')  # This creates a deque with the elements 't', 'e', 's', 't'
a.extend(['a', 'b', 'c'])  # Adds 'a', 'b', and 'c' to the deque

# Iterate over the deque and print each element
for i in a:
    print(i) # Output: t, e, s, t, a, b, c

# in order to print words we can either convert deque to list before extending or
# Push words onto the stack

stack.append('hello')
stack.append('world')
stack.append('python')

# Store the stack after pushing elements in a new variable. In order to store stack in a var first we should do the stack operations then store it in a var

stack1 = list(stack)
print("Stack 1:", stack1)

# Pop words from the stack
print("Popped word:", stack.pop())  # 'python'
print("Popped word:", stack.pop())  # 'world'

# Store the stack after popping elements in a new variable
stack2 = list(stack)
print("Stack 2:", stack2)

# Current state of the stack after popping
print("Stack after popping:", list(stack))

# Push new words based on user input and store the stack at each step
while True:
    word = input("Enter a word (or 'leave blank' to quit): ")
    if word == '':
        break
    stack.append(word)
    # Store the stack after each new word input
    stack3 = list(stack)

# Print the final stack and all previous states of the stack
print("Final stack:", *list(stack))
print("Stack 3:", stack3)

# Print all the stack states stored earlier
print("All stack states:")
print("Stack 1:", stack1)
print("Stack 2:", stack2)
print("Stack 3:", stack3)
