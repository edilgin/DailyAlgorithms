"""
Q: You have two lists [7,1,8,6] and [1,6,3,7,8] find the missing element in one of the lists
A: Again i follow the logic that my friend gurkan found. Summing the items in the right way
   will help us find the missing value. Though if we want to find more than one missing value
   this method wouldnt have worked.
"""
def find_missing(list1, list2):
    print("list1: ", list1,"\nlist2: ", list2)
    print("\nmissing value: ", end="")
    if len(list1) > len(list2):
        # searched item is positive
        if sum(list1) > sum(list2):
            print(sum(list1) - sum(list2))
        # searched item is negative
        else:
            print(-sum(list2)+sum(list1))

    else:
            # searched item is positive
        if sum(list2) > sum(list1):
            print(sum(list2) - sum(list1))
        # searched item is negative
        else:
            print(-sum(list1)+sum(list2))


arr1 = [5,3]
arr2 = [3,5,-4]
find_missing(arr1, arr2)
arr1 = [4,21,9]
arr2 = [9,4,12,21]
find_missing(arr1, arr2)

