#!/usr/local/bin/python2

def sorted_by(a,b):
    a = a.split('.')
    if len(a) == 2:
        a = list(a)
        a.append(-1)
    if len(a) == 1:
        a = list(a)
        a.append(-1)
        a.append(-1)
    b = b.split('.')
    if len(b) == 2:
        b = list(b)
        b.append(-1)
    if len(b) == 1:
        b = list(b)
        b.append(-1)
        b.append(-1)
    a0 = int(a[0])
    b0 = int(b[0])
    a1 = int(a[1])
    b1 = int(b[1])
    a2 = int(a[2])
    b2 = int(b[2])

    if a0 > b0:
        return 1
    if a0 < b0:
        return -1
    if a0 == b0:
        if a1 > b1:
            return 1
        if a1 < b1:
            return -1
        if a1 == b1:
            if a2 > b2:
                return 1
            if a2 < b2:
                return -1
            if a2 == b2:
                return 0

def solution(l):
    l.sort(cmp=sorted_by)
    return l

print solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
