
#Q: Find every combination of a given string

def permutation(arr):
    # if the array only has a single element it means there is only one permutation
    if len(arr) == 1:
        # return that one permutation
        return [arr]
    # empty array but we will populate it
    output = []

    # calculating permutations
    for i in range(len(arr)):
       current_element = arr[i]
       # remaining of a list can be defined as elements until current_element and elements that come
       # after the current_element
       remaining_list = arr[:i] + arr[i+1:]
       # get every permutation as a list and iterate through them
       for p in permutation(remaining_list):
           output.append([current_element] + p)
    return output

string = "abc"
arr1 = [i for i in string]
print(permutation(arr1))
