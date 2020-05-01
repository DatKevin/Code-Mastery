def find_uniq(arr):
    dict = {}
    for num in arr:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    for num in dict:
        if dict[num] == 1:
            return num
