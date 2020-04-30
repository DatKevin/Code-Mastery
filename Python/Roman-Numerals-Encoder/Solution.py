def solution(n):
    answer = []
    print(n)
    if n//1000 >= 1:
        answer.append("M" * (n//1000))
        n -= n//1000 * 1000
    if n//100 == 9:
        answer.append("CM")
        n -= 900
    if n//100 < 9 and n//100 > 4:
        remainder = n//100 % 5
        answer.append("D" + "C" * remainder)
        n -= n//100 * 100
    if n//100 == 4:
        answer.append("CD")
        n -= 400
    if n//100 < 4:
        answer.append("C" * int(n//100))
        n -= n//100 * 100
    if n//10 == 9:
        answer.append("XC")
        n -= 90
    if n//10 < 9 and n//10 > 4:
        remainder = n//10 % 5
        answer.append("L" + "X" * remainder)
        n -= n//10 * 10
    if n//10 == 4:
        answer.append("XL")
        n -= 40
    if n//10 < 4:
        answer.append("X" * int(n//10))
        n -= n//10 * 10
    if n == 9:
        answer.append("IX")
    if n < 9 and n > 4:
        remainder = n % 5
        answer.append("V" + "I" * remainder)
    if n == 4:
        answer.append("IV")
    if n < 4:
        answer.append("I" * int(n))
    return "".join(answer)
