# Array must be sorted to perform binary search


def binary_search(arr, target):
    # return: Index if found, else -1
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2

        # Check if the middle element is the target
        if arr[mid] == target:
            return mid
        # If target is smaller, it must be in the left half, change right point
        elif arr[mid] > target:
            right = mid - 1
        # If target is larger, it must be in the right half, change left point
        else:
            left = mid + 1
    return -1


sorted_list = [1, 3, 5, 7, 9, 11]
