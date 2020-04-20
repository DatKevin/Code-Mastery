def dirReduc(arr):
    dict = {}
    again = True
    opposites = {"NORTH": "SOUTH", "SOUTH": "NORTH","EAST": "WEST", "WEST": "EAST",}
    while again:
        again = False
        for n in range (0, len(arr)):
            if n >= len(arr) - 1:
                break                
            if arr[n] in opposites and arr[n + 1] == opposites[arr[n]]:
                again = True
                del arr[n]
                del arr[n]
                if n >= len(arr) - 1:
                    break                
    return arr
