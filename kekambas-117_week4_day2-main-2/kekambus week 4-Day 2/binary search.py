
Below is a very common logarithmic time function called Binary Search:def binary_search(arr, target):
		left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1