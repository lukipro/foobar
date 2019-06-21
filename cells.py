#!/usr/local/bin/python2

from itertools import combinations

def solution(num_buns, num_req):

    combs = list()
    for comb in combinations(range(num_buns),num_buns-num_req+1):
        combs.append(comb)
        print comb
    print 'num combinations: ' + str(len(combs))

    res = []
    for i in range(num_buns):
        res.append([])

    for i in range(len(combs)):
        for j in combs[i]:
            print 'i: ' + str(i) + ' j: ' + str(j)
            res[j].append(i)
        
    return res

print solution(4,3)
