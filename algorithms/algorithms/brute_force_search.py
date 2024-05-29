def brute_force_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Example usage:
arr = [2, 5, 8, 10, 13, 17]
target = 10
result = brute_force_search(arr, target)
if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the list.")
