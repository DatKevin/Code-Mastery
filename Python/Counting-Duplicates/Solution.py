def duplicate_count(text):
    dic = {}
    for char in text:
        if char.lower() not in dic:
            dic[char.lower()] = 0
        else: 
            dic[char.lower()] += 1
    return len([char for char in dic if dic[char] > 0])
