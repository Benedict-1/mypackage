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


def quick_sort(items):

    if len(items) <= 1:
        return items

    items = list(items)
    pivot = items[-1]
    new_list = [pivot]
    count = 0

    for i in range(len(items)-1):
        if items[i]<pivot:
            new_list = [items[i]]+ new_list
            count+=1
        else:
            new_list = new_list + [items[i]]

    return quick_sort(new_list[:count])+[pivot]+quick_sort(new_list[count+1:])
