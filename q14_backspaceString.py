"""
Q: Write a function that takes two lists and return true if they are equal and false if they are not. If string
   contains # this means backspace a character.
"""

def backspaceString(str1, str2):
    # create two indexes to implement backspaces
    i, j = len(str1) - 1, len(str2) - 1
    # loop will work until both strings are completely checked for backspaces
    while i > 0 and j > 0:
        # if we encounter a # then take all elements until some char "c" and # and take every elements after #
        if str1[i] == "#":
            str1 = str1[:i-1] + str1[i+1:]
            # remove 1 from the index cause we just dealed with a #
            i -= 1
        if str2[j] == "#":
            str2 = str2[:i-1] + str2[i+1:]
            j -= 1
        # remove 1 from the indexes anyway because we need to check the previous elements
        i -= 1
        j -= 1
    # if the calculated strings are equal then return true
    if str1 == str2:
        return True
    return False

flag = backspaceString("abc#", "abc")
print(flag)