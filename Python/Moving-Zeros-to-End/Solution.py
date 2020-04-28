def move_zeros(array):
    count = 0
    for item in array:
        if item == 0 and item is not False:
            print(item)
            count +=1
    array = [char for char in array if char != 0 or char is False]
    for zero in range (count):
        array.append(0)
    return array
