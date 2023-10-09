# LARGEST PRIME FACTOR

def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of integer `n`."""
    i: int = 2

    while i * i <= n: # Prime factors are bounded by i² <= n
        while n % i == 0:
            n = n / i

        if n == 1:
            return i

        i += 1
    
    return int(n)


print(largest_prime_factor(600851475143)) # 6857