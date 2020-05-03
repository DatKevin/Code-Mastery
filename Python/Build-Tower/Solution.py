def tower_builder(n_floors):
    list = []
    floor = 0
    length = (n_floors * 2 - 1)
    for x in range (0, n_floors):
        floor += 1
        x += 1
        stars = x * 2 - 1
        list.append(" " * ((length - stars)//2)  + "*" * stars + " " * ((length - stars)//2))
    return list
