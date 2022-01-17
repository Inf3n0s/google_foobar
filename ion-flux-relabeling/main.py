def generate_child(t,h):
    st = t-(2**(h-1))
    dr = t - 1
    return st, dr

def find_parent(n, h):
    #print("\n\n\n", n)
    ct = 2**h-1
    if n == ct:
        return -1

    while (True):
        st, dr = generate_child(ct, h)
        #print("\n  ", ct, "\n", st, " ", dr, "\n")
        if (n == st or n == dr):
            return ct
        elif (n < st):
            ct = st
        elif (n > st):
            ct = dr
        h -= 1

def solution(h, q):
    # 2**h - 1
    rez = []
    for i in q:
        rez.append(find_parent(i, h))

    return rez