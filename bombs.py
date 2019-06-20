#!/usr/local/bin/python2

def solution(M,F):

#    s = [[tuple([1,1])]]
#
#    #fib = lambda n:pow(2<<n,n+1,(4<<2*n)-(2<<n)-1)%(2<<n)
#
#    #for i in range(300):
#    #    print fib(i)
#    #    if fib(i) > 1e50:
#    #        print i
#    #        break
#
#    for i in range(0,5):
#        temp = []
#        diff = 0
#        maks = 0
#        for n in range(len(s[i])):
#            l = tuple([s[i][n][0], s[i][n][0]+s[i][n][1]])
#            r = tuple([s[i][n][0]+s[i][n][1], s[i][n][1]])
#            temp.append(l)
#            temp.append(r)
#            if s[i][n][0] > maks:
#                maks = s[i][n][0]
#            if s[i][n][1] > maks:
#                maks = s[i][n][1]
#            if abs(s[i][n][0] - s[i][n][1]) > diff:
#                diff = abs(s[i][n][0] - s[i][n][1])
#        #    print abs(s[i][n][0] - s[i][n][1]),
#        s.append(temp)
#        #print 'maks: ' + str(maks) + ' diff: ' + str(diff) +' at i: ' + str(i)
#        print temp[:len(s[i+1])/2]
#
#    #elo = 2
#
#
    gen = 0

    m = int(M)
    f = int(F)

    print '(m, f): (' + str(m) + ', ' + str(f) + ')'
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
                print 'f fits into m ' + str(n)  + ' times'
                gen = gen + n
            else:
                m = m-f
                gen = gen + 1
        elif m < f:
            n = f/m
            if n > 0:
                f = f-n*m
                print 'm fits into f ' + str(n)  + ' times'
                gen = gen + n
            else:
                f = f-m
                gen = gen + 1
        else:
            if m == 1 and f == 1:
                return str(gen)
            else:
                return "impossible"
        print '(m, f): (' + str(m) + ', ' + str(f) + ')'
   
    return str(gen)

    print solution(str(i), str(i+1))
    i = i +1
