# LARGEST PALINDROME PRODUCT

def largest_palindromic_product(n: int) -> int:
    """Return the largest palindromic product of integers length `n`."""
    largest_product: int = 0

    for x in range(10 ** n - 1, 100, -1):
        # OPTIMISATION: break if x² < largest product
        if x * x < largest_product:
            break

        for y in range(x, 10 ** (n - 1), -1):
            product: int = x * y

            # OPTIMISATION: break if product < largest product
            if product < largest_product:
                break

            if (str_product := str(product)) == str_product[::-1]:
                largest_product = product

    return largest_product


print(largest_palindromic_product(3)) # 906609