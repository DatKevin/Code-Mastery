def encode_str(strng, shift):
    message = []
    alphabet = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25,"z":26}
    message.append(strng[0].lower())
    count = 0
    for char in strng:
        if char.lower() in alphabet:
            newlet = alphabet[char.lower()] + shift
            if newlet > 26:
                newlet -=26
            if count == 0:
                message.append([new for new in alphabet if alphabet[new] == newlet][0])
                count += 1
            if char.isupper():
                message.append([new for new in alphabet if alphabet[new] == newlet][0].upper())
            else:
                message.append([new for new in alphabet if alphabet[new] == newlet][0])
        else:   
            message.append(char)
    length = len(message) // 5
    answer = []
    if len(message) % 5 == 0:
        for num in range (1, 6):
            answer.append("".join(message[(num - 1)*length: num*length]))
        return answer
    else:
        fifth = len(message) - (length * 4)
        while length < fifth:
            length += 1
            fifth -= 4
        for num in range (1, 5):
                answer.append("".join(message[(num - 1)*length: num*length]))
        if fifth != 0:
            answer.append("".join(message[length*4:]))          
        return answer
    
def decode(arr):
    alphabet = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25,"z":26}
    shift = alphabet[arr[0][1]] - alphabet[arr[0][0]]
    if shift < 0:
        shift += 26
    arr = "".join(arr)
    answer = []
    count = 0
    for char in arr:
        if count < 2:
            count += 1
        elif char.lower() in alphabet:
            newlet = alphabet[char.lower()] - shift
            if newlet < 0:
                newlet +=26
            if char.isupper():
                answer.append([new for new in alphabet if alphabet[new] == newlet][0].upper())
            else:
                answer.append([new for new in alphabet if alphabet[new] == newlet][0])
        else:   
            answer.append(char)
    return("".join(answer))