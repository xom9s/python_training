def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # If left child exists and is greater than root
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # If right child exists and is greater than largest so far
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # If largest is not root, then swap and heapify the affected sub-tree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

# Example usage:
arr = [19, 2, 31, 45, 30, 11, 121, 27]
heap_sort(arr)
print(arr)