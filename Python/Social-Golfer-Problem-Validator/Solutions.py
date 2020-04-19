def valid(a):
    dict = {}
    count = 0
    for day in a:
        if len(day) != len(a[0]):
            return False
        for group in day:
            if len(group) != len(a[0][0]):
                return False
            for golfer in group:
                if golfer not in dict:
                    if count == 0:
                        dict[golfer] = {}
                    else: 
                        return False
                others = [ person for person in group if person != golfer]
                for person in others:
                    if person not in dict[golfer]:
                        dict[golfer][person] = True
                    else:
                        return False
        count += 1
    return True
