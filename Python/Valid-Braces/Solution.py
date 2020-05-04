def validBraces(string):
    loopagain = True
    while loopagain == True:
        loopagain = False
        if string.find("()") >= 0:
            loopagain = True
            string = string.replace("()","")
        if string.find("{}") >= 0:
            loopagain = True
            string = string.replace("{}","")
        if string.find("[]") >= 0:
            loopagain = True
            string = string.replace("[]","")
    if string:
        return False
    else: 
        return True
