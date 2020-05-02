def alphabet_war(battlefield):
    survivors = []
    if "#" not in battlefield:
        return "".join([char for char in battlefield if char != "[" and char !="]" and char != "#"])
    string = battlefield.split("[")
    for num in range (1, len(string)):
        count = 0
        for char in string[num - 1]:
            if char == "#":
                count += 1
        for char in string[num]:
            if char == "#":
                count += 1
        if count <= 1:
            survivors.append(string[num])
    answer = []
    for text in survivors:
        for char in text:
            if char == "]":
                break
            answer.append(char)
    answer = [char for char in answer if char != "]"]
    return "".join(answer)
