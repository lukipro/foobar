#!/usr/local/bin/python2

def solution(M,F):

    gen = 0

    m = int(M)
    f = int(F)

    while(True):
        if m <= 0 or f <= 0:
            return "impossible"

        if m == 1 and f > 1:
            return str(gen + f - 1)

        if f == 1 and m > 1:
            return str(gen + m - 1)

        if m > f:
            n = m/f
            if n > 0:
                m = m-n*f
                gen = gen + n
            else:
                m = m-f
                gen = gen + 1
        elif m < f:
            n = f/m
            if n > 0:
                f = f-n*m
                gen = gen + n
            else:
                f = f-m
                gen = gen + 1
        else:
            if m == 1 and f == 1:
                return str(gen)
            else:
                return "impossible"
   
    return str(gen)

print solution('100000000000000000000000000000000000000000000000000', '7')
