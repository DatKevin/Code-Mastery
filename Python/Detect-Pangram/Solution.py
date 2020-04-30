import string

def is_pangram(s):
    dict = {}
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",] 
    for char in s:
        if char.lower() not in dict:
            dict[char.lower()] = 1
    for letter in alphabet:
        if letter not in dict:
            return False
    return True
