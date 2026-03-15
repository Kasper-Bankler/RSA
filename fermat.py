# Python 3 implementation of fermat's factorization
# https://www.geeksforgeeks.org/fermats-factorization-method/

from math import ceil, sqrt
import time

# This function finds the value of a and b
# and returns a+b and a-b


def FermatFactors(n):
    iterations = 0
    # since fermat's factorization applicable
    # for odd positive integers only
    if (n <= 0):
        return [n]

    # check if n is a even number
    if (n & 1) == 0:
        return [n / 2, 2]

    a = ceil(sqrt(n))

    # if n is a perfect root,
    # then both its square roots are its factors
    if (a * a == n):
        return [a, a]

    while (True):
        iterations += 1
        b1 = a * a - n
        b = int(sqrt(b1))
        if (b * b == b1):
            break
        else:
            a += 1
    print(f"{iterations} iterations")
    return [a-b, a + b]


# Driver Code
# Starting timer
start_time = time.time()

print(FermatFactors(388834419354339699899))

# Printing time and peak memory usage
print("\nTime: %s seconds" % (time.time() - start_time))
