def memory(f):
    dict = {}
    def inner(n):
        if n in dict:
            return dict[n]
        else:
            dict[n] = f(n)
        return dict[n]
    return inner

@memory
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
