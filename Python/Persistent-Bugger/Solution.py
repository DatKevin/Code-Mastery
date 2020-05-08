
def persistence(n):
    start = n
    count = 0
    while len(str(start)) > 1:
        newnum = start
        count += 1
        start = 1
        for digit in str(newnum):
            start = int(digit) * start
    return count
