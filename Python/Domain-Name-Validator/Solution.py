def validate(domain):
    validchar = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    validsymbols = ["-", "."]
    count = 0
    for char in domain:
        if char not in validchar and char not in nums and char not in validsymbols:
            return False
        if char == ".":
            count += 1      
    if count > 0 and count <= 126 and len(domain) <= 253:
        split = domain.split(".")
        allnumbers = False
        for sublevel in split:
            if len(sublevel) > 0:
                if sublevel[0] in validsymbols or sublevel[len(sublevel) - 1] in validsymbols:
                    return False
            if len(sublevel) > 63 or len(sublevel) == 0:
                return False
            for char in sublevel:
                if char not in nums:
                    allnumbers = True
                    break
        topallnums = False
        for char in split[len(split) - 1]:
            if char not in nums:
                topallnums = True
                break
        return allnumbers and topallnums
    else:
        return False
