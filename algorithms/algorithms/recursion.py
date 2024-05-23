def tail_recursive_factorial(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return tail_recursive_factorial(n-1, n*accumulator)

# Example usage:
print(tail_recursive_factorial(5))  # Output: 120
    
def non_tail_recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * non_tail_recursive_factorial(n - 1)

# Example usage:
print(non_tail_recursive_factorial(5))  # Output: 120