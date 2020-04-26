def score(dice):
    dict = {}
    print(dice)
    score = 0
    for num in dice:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    for num in dict:
        if dict[num] >= 3:
            if num in range(2, 7):
                score += num * 100
                print(score)
            else:
                score += 1000
            dict[num] -= 3
        if num == 1:
            score += 100 * dict[num]
        if num == 5:
            score += 50 * dict[num]
    return score

