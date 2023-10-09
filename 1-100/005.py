# SMALLEST MULTIPLE

def gcd(x: int, y: int) -> int:
    """Return the GCD (greatest common denominator) of `x` and `y`."""
    while y:
        x, y = y, x % y

    return x

def lcm(x: int, y: int) -> int:
    """Return the LCM (lowest common multiple) of `x` and `y`."""
    return x * y // gcd(x, y)


def smallest_multiple(n: int) -> int:
    """Return the smallest multiple of integers up to `n`."""
    smallest_multiple: int = 1
    
    for i in range(1, n + 1):
        smallest_multiple = lcm(smallest_multiple, i)

    return smallest_multiple


print(smallest_multiple(20)) # 232792560