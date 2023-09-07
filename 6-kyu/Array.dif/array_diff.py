def array_diff(a, b):
    for element in b:
        for i in range(0, a.count(element)):
            a.remove(element)
    return a
