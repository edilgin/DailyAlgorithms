"""
Q: Write a function that returns True if a string is a palindrome. Use a stack.
A: My algorithm will be:
    1- Find the midpoint of the string
    2- Check if length of the string is even or odd and based on that
    split the string from the middle
    3- Add left side of the string to one stack and the right side to another stack
    4- pop values of both of the stacks and check if they are the same. This should be done
    until the stacks are empty
    5- Return True or False based on the 4.step
"""

def check_palindrome_longversion(word):
    # a boolean for returning True or False
    equal = True
    # midpoint will be used for determining words midpoint
    midpoint = int(len(word) / 2)
    length = len(word)

    # we must check if length of the word is even or odd because that will change what we add to
    # to stack

    # if words length is even
    if length % 2 == 0:
        # stack_left is left side of the string
        stack_left = [i for i in word[0:midpoint]]
        # stack_right is the right side of the string
        stack_right = [i for i in word[length:midpoint-1:-1]]

    # if words length is odd
    else:
        stack_left = [i for i in word[0:midpoint]]
        stack_right = [i for i in word[length:midpoint:-1]]

    for i in range(len(stack_left)):
        # compare every value of the stacks by popping elements from each of them
        boolean = (stack_left.pop() == stack_right.pop())
        # if there is a difference
        if boolean != True:
            # they are no longer equal
            equal = False
            break

    return equal


# not a readable code but it is short
def check_palindrome_shortversion(word):
    if len(word) % 2 == 0:
        stack_left = [i for i in word[0:int(len(word) / 2)]]
        stack_right = [i for i in word[len(word):int(len(word) / 2)-1:-1]]
    else:
        stack_left = [i for i in word[0:int(len(word) / 2)]]
        stack_right = [i for i in word[len(word):int(len(word) / 2):-1]]
    if len([i for i in range(len(stack_left)) if stack_left.pop() != stack_right.pop()]) > 0:
        return False
    return True

# these will return true
flag = check_palindrome_shortversion("mmmmammmm")
print(flag)
flag = check_palindrome_shortversion("lool")
print(flag)
# these will return false
flag = check_palindrome_shortversion("mmmma")
print(flag)
flag = check_palindrome_shortversion("keke")
print(flag)
