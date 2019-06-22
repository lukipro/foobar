#!/usr/local/bin/python2

import numpy as np
import fractions

def solution(m):
    mat = np.matrix(m)

    i = 0
    term_states = []
    temp_states = []
    for row in mat:
        if np.sum(row) == 0:
            term_states.append(i)
        else:
            temp_states.append(i)
        i = i+1

    if 0 in term_states:
        return np.array([1,1])

    d = []
    for n in temp_states:
        s = 0
        i = 0
        for m in mat[n,:].flat:
            if i in term_states:
                s = s + m
            i = i + 1
        d.append(np.float(s)/np.sum(mat[n,:]))
    A = np.diag(d)

    B = np.zeros((len(temp_states), len(temp_states)))
    i = 0
    for n in temp_states:
        for m in temp_states:
            if mat[n,m] > 0:
                B[temp_states.index(m), i] = np.float(mat[n,m])/np.sum(mat[n,:])
        i = i+1

    I = np.identity(len(temp_states))
    S = np.dot(A,np.linalg.inv(I-B))

    O = np.zeros((len(temp_states), len(term_states)))
    l = 0
    for i in temp_states:
        s = 0
        k = 0
        for j in range(np.size(mat[n,:],1)):
            if j in term_states:
                s = s+mat[i,j]
                O[l,k] = mat[i,j]
                k = k+1
        if s != 0:
            O[l,:] = O[l,:]/s
        l = l+1

    R = np.dot(np.transpose(S), O)

    nums = []
    dens = []
    for j in range(np.size(R,1)):
        f = fractions.Fraction(R[0,j]).limit_denominator()
        nums.append(f.numerator)
        dens.append(f.denominator)

    kk = np.lcm.reduce(dens)
    mult = kk/dens
    res = np.multiply(mult, nums)
    res = np.append(res,kk)

    return res

print solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
