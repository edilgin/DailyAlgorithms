"""
Q: Find if two words are anagram
A:  We will turn both strings into a list. Then we will change their value to their ASCII
    value. After that quick sort algorithm will be implemented to sort the lists. Quick sort
    algorithm is picked because it has a nlogn time complexity and nlogn space
    complexity. Lastly we will compare the two lists and if they are the same we will say
    the two words are anagram.
"""

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i


def quick_sort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quick_sort(arr, left, partition_pos - 1)
        quick_sort(arr, partition_pos + 1, right)


def anagram(word1, word2):
    list1 = [char for char in word1]
    list2 = [char for char in word2]

    quick_sort(list1, 0, len(list1) - 1)
    quick_sort(list2, 0, len(list2) - 1)

    if list1 == list2:
        return True

    else:
        return False


flag = anagram("oop","poo")
print("anagram durumu: ", flag)

flag = anagram("keko bir adam","damak korebi ")
print("anagram durumu: ", flag)

