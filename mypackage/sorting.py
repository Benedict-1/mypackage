def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    count = 0
    for idx in range(len(items)-1):
        if items[idx] > items[idx + 1]:
            items[idx],items[idx + 1] = items[idx + 1],items[idx]
            count += 1

    if count == 0:
        return items
    else:
        return bubble_sort(items)

def merge(left, right):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(array):
    """Merge sort algorithm implementation."""

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    return merge(left, right)


def partition(array, begin, end):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx



def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def quick_sort_recursion(array, begin, end):
        if begin >= end:
            return
        pivot_idx = partition(array, begin, end)
        quick_sort_recursion(array, begin, pivot_idx-1)
        quick_sort_recursion(array, pivot_idx+1, end)

    return quick_sort_recursion(array, begin, end)
