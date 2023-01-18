# Algorithme récursif
def binary_search_recursive(arr, x, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return binary_search_recursive(arr, x, mid + 1, end)
    else:
        return binary_search_recursive(arr, x, start, mid - 1)