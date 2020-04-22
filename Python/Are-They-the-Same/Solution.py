def comp(array1, array2):
    dict = {}
    dict2 = {}
    if array2 == None or array1 == None or len(array1) == 0 or len(array2) == 0:
        return array2 == array1
    for num in array2:
        if num in dict2:
            dict2[num] += 1
        else:
            dict2[num] = 1
    array1 = [num**2 for num in array1]
    for num in array1:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    return len({num: dict[num] for num in dict if num in dict2 and dict[num] == dict2[num]}) == len(dict)
