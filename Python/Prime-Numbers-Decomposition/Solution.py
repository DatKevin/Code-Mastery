 
def getAllPrimeFactors(n):
    result = []
    if type(n) != type(1):
        return []
    if n == 1 or n == 2:
        return [n]
    for num in range (2, n):
        if n % num == 0:
            while n % num == 0:
                n /= num
                result.append(num)
            if n == 1:
                break
    return result
                  

def getUniquePrimeFactorsWithCount(n):
    prime = []
    power = []
    if type(n) != type(1):
        return [[], []]
    if n == 1 or n == 2:
        return [[n],[1]]
    for num in range (2, n):
        if n % num == 0:
            count = 0
            while n % num == 0:
                n /= num
                count += 1
            prime.append(num)
            power.append(count)
            if n == 1:
                break
    return [prime, power]


def getUniquePrimeFactorsWithProducts(n):
    result = []
    primes = []
    if type(n) != type(1):
        return []
    if n == 1 or n == 2:
        return [n]
    for num in range (2, n):
        if n % num == 0:
            count = 0
            while n % num == 0:
                n /= num
                count += 1
            primes.append([count, num])
            if n == 1:
                break
    for prime in primes:
        result.append(prime[1] ** prime[0])
    return result
