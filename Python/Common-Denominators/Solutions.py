def convertFracts(lst):
    answer = []
    dict = {}
    for item in lst:
        sub = item[1]
        for num in range (2, sub + 1):
            count = 0
            while sub % num == 0:
                count +=1
                sub /= num
            if count >= 1:
                if num not in dict or count > dict[num]:
                    dict[num] = count
    product = 1
    for prime in dict:
        product *= prime ** dict[prime]
    for num in lst:
        num = [ int * (product // lst[lst.index(num)][1]) for int in num]
        answer.append(num)
    return answer