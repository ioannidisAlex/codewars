def digit_zeroer(n):
		for i in range(0, len(str(n))-1):
        u = n % 10
        n = n // 10;
        if u != 0:
            return 0;
    return 1;

def same_digits(n):
    if str(n) == str(n)[0] * len(str(n)):
        return 1
    else:
        return 0;

def inc_rec(start,build,lst):
    if build % 10 == 9: 
        lst.append(build*10+start-9)
        return
    inc_rec(start+1, build*10+start+1, lst)
    lst.append(build*10+start+1)
    #r_lst.append(("1" * len(str(build*10+start+1))) - )

def dec_rec(start,build,r_lst):
    if build % 10 == 0: return
    dec_rec(start-1, build*10+start-1, r_lst)
    r_lst.append(build*10+start-1)    
    
def sequential_digits(n):
    lst = []
    r_lst = []
    for i in range(1,9):
        inc_rec(i,i,lst)
    lst.append(90)
    for i in range(1,9):
        dec_rec(10-i,10-i,r_lst)
    if (n in lst or n in r_lst):
        return 1
    else:
        return 0

def palindrome_sequence(n):
    if str(n) == str(n)[::-1]:
        return 1
    else:
        return 0

def is_interesting(number, awesome_phrases):
    if number == 99 or number == 98: return 1
    if len(str(number)) < 3: return 0
    if palindrome_sequence(number) or digit_zeroer(number) or same_digits(number): return 2
    if sequential_digits(number) or (number in awesome_phrases): return 2
    numbers = [number+1, number+2]
    for num in numbers:
        if palindrome_sequence(num) or digit_zeroer(num) or same_digits(num): return 1
        if sequential_digits(num) or (num in awesome_phrases): return 1
    return 0
