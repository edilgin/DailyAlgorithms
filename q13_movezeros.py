"""
Q: You are given an array like [1,4,0,7,0,2,9], create a function which moves zeros to the end of the list while
   maintaining the order of the list like this: [1,4,7,2,9,0,0]
"""

def moveZeros(arr):
    sortedArr = []
    end_index = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            sortedArr.insert(end_index, arr[i])
            end_index += 1
        else:
            sortedArr.append(0)
    return sortedArr

arr1 = [3,0,4,0,1,7,8,0,10]
sortedarr = moveZeros(arr1)
print(sortedarr)