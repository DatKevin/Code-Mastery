def scramble(s1, s2):
    dict = {}
    for char in s1:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    for char in s2:
        if char in dict:
            dict[char] -= 1
            if dict[char] < 0:
                return False
        else:
            return False
    return True
