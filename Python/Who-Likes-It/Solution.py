
def likes(names):
    if len(names) == 0:
        return "no one likes this"
    if len(names) == 1:
        return (names[0] + " likes this")
    else:
        if len(names) > 2:
            names[0] = names[0] + ","
        if len(names) < 4:
            names.insert(-1, "and")
            names.insert(len(names), "like this")
            return " ".join(names)
        else:
            others = str(len(names) - 2)
            names.insert(2, f"and {others} others like this")
            return " ".join(names[:3])
