"""
Q: You have an array with duplicate values and there is only one value which doesnt repeat. Return that one value.
For example if you have a list [3, 7, 4, 3, 5, 4, 7] => 5

A: We can use xor for this and have a time complexity of O(N). Proof is below
        for example for array [9,1,2,9,7,1,7]
        0 ^ 9 = x
        x ^ 1 = y
        y ^ 2 = z
        z ^ 9 = k
        k ^ 7 = l
        l ^ 1 = m
        m ^ 7 = n
        the equation turns in to:
        0 ^ 9 ^ 1 ^ 2 ^ 9 ^ 7 ^ 1 ^ 7
        and since in xor you can change the position of the elements:
        0 ^ (9 ^ 9 ) ^ (1 ^ 1) ^ (7 ^ 7) ^ 2 = 0 ^ 0 ^ 0 ^ 0 ^ 2 = 2
"""
def isSingle(arr):
    temp = 0
    for item in arr:
        temp = temp ^ item
    return temp

arr1 = [9,1,2,9,7,1,7]
print(isSingle(arr1))
arr2 = [3, 7, 4, 3, 5, 4, 7]
print(isSingle(arr2))
