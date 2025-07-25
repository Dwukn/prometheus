# in order to reverse the stack we can either use recursion or we can use a while loop to pop elements from the stack and append them to a new stack
# Reverse a stack using a while loop

def reverse_stack(stack):
    reversed_stack = []
    print("Stack: ",stack)  # Output: [a, b, c, d, e]
    while stack:
        reversed_stack.append(stack.pop())
    return reversed_stack

# Reverse a stack using recursion
# stores pop element in a temperary variable and then calls the function recursively and then inserts the element at the 0th index of the stack
def recursive_reverse_stack(stack):
    if len(stack) == 0:
        return stack
    temp = stack.pop()
    # print("Temp: ",temp) #output: e | d | c | b | a
    recursive_reverse_stack(stack)
    stack.insert(0, temp)
    return stack


def main():
    # Reverse the stack
    stack = ['a', 'b', 'c', 'd', 'e']
    stack2 = ['a', 'b', 'c', 'd', 'e']
    reversed_stack = reverse_stack(stack)
    recursive_reverse = recursive_reverse_stack(stack2)
    print("reverse stack: ",reversed_stack)  # Output: ['e', 'd', 'c', 'b', 'a']
    print("recursive reverse stack: ",recursive_reverse)  # Output: ['e', 'd', 'c', 'b', 'a']

main()
