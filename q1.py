
# If less than 2, it isnt prime.
# loop i till square root of x with +1 because range exclude int(x ** 0.5)
# if divisible then not prime
def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def getPrimeNumbers(n):
    primes = []
    for x in range(2, n+1):
        if isPrime(x):
            primes.append(x)
    return primes
print(getPrimeNumbers(100))