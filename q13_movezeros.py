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