
def is_descending(arr):
    elements = [10]
    for idx, item in enumerate(arr):
        if elements[idx] < item:
            return False

        elements.append(item)
    return True


def get_low_swap(arr):
    i = len(arr) - 2
    while i > -1:
        if arr[i] < arr[i+1]:
            return i
        i = i - 1

def get_highest_index_greater_than_low_swap(arr, low_swap):
    i = len(arr) - 1
    while i > low_swap:
        if arr[i] > arr[low_swap]:
            return i
        i = i - 1

def swap(low, high, arr):
    newArr = arr.copy()
    newArr[low] = arr[high]
    newArr[high] = arr[low]
    return newArr

def next_permutation(arr):
    if is_descending(arr):
        arr.reverse()
        return arr

    # find the first case where arr[i] < arr[i+1]
    low_swap = get_low_swap(arr)
    high_swap = get_highest_index_greater_than_low_swap(arr, low_swap)

    arr = swap(low_swap, high_swap, arr)

    # reverse the rest of the list
    part_to_reverse = arr[low_swap+1:]
    part_to_reverse.reverse()

    return arr[:low_swap + 1] + part_to_reverse


print(next_permutation([1,2,3]) == [1,3,2])
print(next_permutation([1,3,2]) == [2,1,3])
print(next_permutation([3,1,2]) == [3,2,1])
print(next_permutation([3,2,1]) == [1,2,3])
