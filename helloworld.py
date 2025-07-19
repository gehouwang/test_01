def primes_sieve(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i: n+1: i] = [False] * len(sieve[i*i: n+1: i])
    return [i for i, prime in enumerate(sieve) if prime]

# 输出100以内所有素数
print(primes_sieve(100))
