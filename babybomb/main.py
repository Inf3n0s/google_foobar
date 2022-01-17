from math import floor
from operator import truediv


def aregood(m,f):
    if(m==1 and f==1):
        return True
    if(m>0 and f>0):
        if(m != f):
            return True
    return False

def solution(m,f):
    m = int(m)
    f = int(f)
    step = -1
    while(m>1 or f>1):
        if(aregood(m,f)==False):
            return "impossible"
        else:
            if(m>f):
                step += m//f
                m=m-f*(m//f)
            else:
                step += f//m
                f=f-m*(f//m)
    return str(step)


print(aregood(2,4))
print(solution(4,7))
