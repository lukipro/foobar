#!/usr/local/bin/python2

import itertools

def solution(l):
    solution = 0
    for i in range(len(l)+1):
        for s in list(itertools.permutations(l,i)):
            sum = 0
            for c in s:
                sum = sum + int(c)
            if sum % 3 == 0:
                if len(s):
                    maybe = int(''.join(str(c) for c in s))
                    if maybe > solution:
                        solution = maybe
            else:
                continue
    return solution

print solution([3, 1, 4, 1, 5, 9])
print solution([3, 1, 4, 1])
