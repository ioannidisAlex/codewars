def find_it(seq):
    for i in set(seq):
        if seq.count(i) % 2 == 1:
            return i
