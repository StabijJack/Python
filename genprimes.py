def genPrimes():
    primes = []
    n=1
    while True:
        n += 1
        isPrime = True
        for p in primes:
            if (n % p) == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(n)
            yield n
gP=genPrimes()
print(gP.__next__())