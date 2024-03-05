def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  
my_list = [5, 3, 8, 2, 9, 1]
target_value = 8
result = linear_search(my_list, target_value)
if result != -1:
    print(f"Target value {target_value} found at index {result}.")
else:
    print(f"Target value {target_value} not found in the list.")
