def isPP(n):
    for num in range (2, n//2 + 1):
        number = n
        count = 0
        while number % num == 0:
            count += 1
            number /= num
        if number == 1:
            return [num, count]
    else:
        return None
