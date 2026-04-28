import math
from PrimeFinder import generatePrimes
from sympy import isprime, factorint


if __name__ == "__main__":
    prime_list = generatePrimes(100)
    prime_product = 1
    for i in prime_list:
        if i == 2:
            continue
        prime_product *= i
        temp = prime_product + 4
        if not isprime(temp):
            print(f"Found a counterexample: {i} {temp:70} {factorint(temp)}")
