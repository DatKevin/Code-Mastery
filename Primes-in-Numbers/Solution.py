def primeFactors(n):
    answer = []
    for prime in range (2, n):
        count = 0
        while n % prime == 0:
            n /= prime
            count += 1
        if count == 1:
            answer.append("(" + str(prime) + ")")
        if count >= 2:
            answer.append("(" + str(prime) + "**" + str(count) + ")") 
        if n == 1:
            return "".join(answer)
    if len(answer) == 0:
        return "(" + str(n) + ")"
    else:
        return "".join(answer)
