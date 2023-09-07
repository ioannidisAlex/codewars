def move_zeros(array):
    array_zeros = []
    array_end = [x for x in array if x != 0]
    for i in range(len(array) - len(array_end)):
        array_zeros.append(0)
    array_end.extend(array_zeros)       
    return array_end
