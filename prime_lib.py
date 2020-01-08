# - This is an implementation of an algorithm called "Sieve of Eratosthenes"
# which accepts a number let's call it n, and outputs a list of all the prime numbers up to hat number.
# - by Musaab Shalek
def s_e(n):
    primes = [True for i in range(n)]
    i = 2
    while(i*i < n):
        if primes[i] == True:
            for j in range(i**2, n, i):
                primes[j] = False

        i += 1

    result = [m for m in range(2, n) if primes[m]]
    return result

# - is_prime returns True if n is prime otherwise it returs False
def is_prime(n):
    counter = 0
    for i in s_e(int(n**0.5)):
        if n%i == 0: return False
        else: counter += 1
    return True
