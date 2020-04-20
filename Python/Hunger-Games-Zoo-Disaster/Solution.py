def who_eats_who(zoo):
    eatingdict = {"antelope": "grass", "big-fish": "little-fish", "bug":"leaves", "bear": ["big-fish", "bug", "chicken", "cow", "leaves", "sheep"], "chicken":"bug","cow":"grass", "fox":["chicken", "sheep"], "giraffe":"leaves", "lion":["antelope", "cow"], "panda":"leaves", "sheep":"grass"}
    copy = zoo.split(",")
    answer = []
    answer.append(zoo)
    again = True
    while again:
        again = False
        for num in range(0, len(copy)):
            if copy[num] in eatingdict:
                if num != 0:
                    if copy[num - 1] in eatingdict[copy[num]]:
                        answer.append(f"{copy[num]} eats {copy[num - 1]}")
                        del copy[num - 1]
                        again = True
                        break
                if num < len(copy) - 1:
                    if copy[num + 1] in eatingdict[copy[num]]:
                        answer.append(f"{copy[num]} eats {copy[num + 1]}")
                        del copy[num + 1]
                        again = True
                        break
    answer.append(",".join(copy))
    return answer
