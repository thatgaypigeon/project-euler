# MULTIPLES OF 3 OR 5

def sum_multiples(n: int) -> int:
    """Return the sum of multiples of 3 or 5 up to `n`."""
    sum: int = 0

    for i in range(1, n):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i

    return sum


print(sum_multiples(1000)) # 233168