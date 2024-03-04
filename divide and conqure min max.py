def find_max_min(arr, left, right):
    if left == right:
        return arr[left], arr[left]
    if right - left == 1:
        return (arr[left], arr[right]) if arr[left] < arr[right] else (arr[right], arr[left])
    mid = (left + right) // 2
    max_left, min_left = find_max_min(arr, left, mid)
    max_right, min_right = find_max_min(arr, mid + 1, right)
    return max(max_left, max_right), min(min_left, min_right)
arr = [3, 5, 1, 9, 2, 7, 4, 8]
max_element, min_element = find_max_min(arr, 0, len(arr) - 1)
print("Maximum element:", max_element)
print("Minimum element:", min_element)

