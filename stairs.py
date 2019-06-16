#!/usr/local/bin/python2

a = []
q = []
k = []

def ak(k):
    if k in a and k != 0:
        return 1
    elif -k in a and k != 0:
        return -1
    else:
        return 0

def qk(k):
    if k == 0:
        return 1
    else:
        qkk = ak(k)
        for i in get_offsets(k):
            if i > 0:
                qkk = qkk - q[k-i]
            else:
                qkk = qkk + q[k+i]
        return qkk

def get_offsets(n):
    offsets = []
    for i in range(len(k)):
        if abs(k[i]) <= n:
            if abs(k[i]) > 0:
                offsets.append(k[i])
        else:
            break
    return offsets

def solution(n):
    for m in range(n):
        k.append((3*m*m-m)/2*(-1)**m)
        k.append((3*m*m+m)/2*(-1)**m)
    
    for m in range(n):
        a.append((3*m*m-m)*(-1)**m)
        a.append((3*m*m+m)*(-1)**m)
    
    for i in range(n+1):
        q.append(qk(i))

    return q[n]-1

solution(200)
