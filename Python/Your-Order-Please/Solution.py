def order(sentence):
    sentence = sentence.split(" ")
    answer = []
    for num in range (1,10):
        word = [word for word in sentence if str(num) in word]
        if word != []:
            answer.append(word[0])
    return " ".join(answer)
