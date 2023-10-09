# EVEN FIBONACCI NUMBERS

def sum_fibonacci(end: int) -> int:
    """Return the sum of even Fibonacci numbers up to `n`."""
    sum: int = 0

    x: int = 1
    y: int = 2

    while x < 4_000_000:
        if x % 2 == 0:
            sum += x

        x, y = y, x + y
    
    return sum


print(sum_fibonacci(4_000_000)) # 4613732