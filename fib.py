def fibonacci(n):
    """
    This function returns the nth Fibonacci number.
    The Fibonacci sequence is as follows: 0, 1, 1, 2, 3, 5, 8, 13, ...
    So fibonacci(1) returns 0, fibonacci(2) returns 1, etc.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

# Test the function by calculating the first 10 Fibonacci numbers
fibonacci_numbers = [fibonacci(i) for i in range(1, 11)]
print(fibonacci_numbers)
