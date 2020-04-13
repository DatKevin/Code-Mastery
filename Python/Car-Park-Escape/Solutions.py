def escape(carpark):
    result = []
    startfloor = 0
    for floornum in range(0, len(carpark)):
        if 2 in carpark[floornum]:
            startfloor = floornum
            break
    current = carpark[startfloor].index(2)
    for floornum in range(startfloor, len(carpark)):
        if 1 in carpark[floornum]:
            move = carpark[floornum].index(1) - current
            current = carpark[floornum].index(1)
            if move > 0:
                result.append("R{}".format(move))
            if move < 0:
                result.append("L{}".format(move * -1))
            result.append("D1")
        if (floornum + 1) == len(carpark):
            move = len(carpark[floornum]) - current - 1
            if move > 0:
                result.append("R{}".format(move))
    for movenum in range(0, len(result)):
        if movenum >= len(result) - 1:
            break
        if result[movenum] == result[movenum + 1]:   
            downcount = 1
            while result[movenum] == result[movenum + 1]:
                del result[movenum + 1]
                downcount += 1
                if movenum == len(result) - 1:
                    break
            result[movenum] = "D{}".format(downcount)
    return result

