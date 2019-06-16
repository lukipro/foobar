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
    print 'calling qk(' + str(k) + ')'
    if k == 0:
        print 'returning q[' + str(k) + '] = ' + str(1)
        return 1
    else:
        qkk = ak(k)
        print 'adding +a[' + str(k) + '] = ' + str(ak(k))
        print 'offsets: ' + str(get_offsets(k))
        for i in get_offsets(k):
            if i > 0:
                print '-q[' + str(k-i) + '] = ' + str(-q[k-i])
                qkk = qkk - q[k-i]
            else:
                print '+q[' + str(k+i) + '] = ' + str(q[k+i])
                qkk = qkk + q[k+i]
        print 'returning q[' + str(k) + '] = ' + str(qkk)
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
    
    print 'k: ' + str(k) 
    
    for m in range(n):
        a.append((3*m*m-m)*(-1)**m)
        a.append((3*m*m+m)*(-1)**m)
    
    print 'a: ' + str(a) 

    for i in range(n):
        print 'a(' + str(i) + '): ' + str(ak(i))


    for i in range(n+1):
        q.append(qk(i))

    print q


solution(200)
