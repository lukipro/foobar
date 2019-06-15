#!/usr/local/bin/python2
import numpy as np
import fractions

def solution(m):
    mat = np.matrix(m)
    print mat
    
    i = 0
    term_states = [] # list of terminal states of the ore
    temp_states = [] # list of temporary states of the ore
    for row in mat:
        if np.sum(row) == 0: # if the row is empty the the state is terminal
            term_states.append(i)
        else:
            temp_states.append(i)
        i = i+1

    print 'Terminal  states: ' + ''.join(str(term_states))
    print 'Temporary states: ' + ''.join(str(temp_states))

    d = [] # list of probabilities of transitioning from a temporary state to a terminal state
    for n in temp_states: # iterate over rows of temporary states
        s = 0 # initialize sum to zero
        i = 0
        for m in mat[n,:].flat: # iterate over probabilities of moving from a temp state
            if i in term_states:
                s = s + m # if the move is to terminal state then increase the overall probablity
            i = i + 1
        d.append(np.float(s)/np.sum(mat[n,:])) # append normalized probability
    A = np.diag(d)
    print 'Probabilities of transisions to terminal states from temporary states:'
    print A

    # matrix showin probabilities of going from one temp state to another
    # index [0,1] - probablity of going from second temp state to first temp state
    # index [1,0] - probablity of going from first  temp state to second temp state
    # index [1,2] - probablity of going from third  temp state to second temp state
    B = np.zeros((len(temp_states), len(temp_states)))
    i = 0
    for n in temp_states: # iterate over rows of temp states
        for m in temp_states: # at each row iterate one more time over temp states
            if mat[n,m] > 0: # if there is a probability of going from the n temp state to the m temp state, then place that normalized probability into B
                B[temp_states.index(m), i] = np.float(mat[n,m])/np.sum(mat[n,:])
        i = i+1
    print 'Overall probability of eventually getting to a terminal state:'
    print B

    # P_xterm = A*x + A*B*x + A*B*B*x ... = A(I + B + B^2 ...)x = A(I-B)^-1 * x
    I = np.identity(len(temp_states))
    S = np.dot(A,np.linalg.inv(I-B))
    print 'Probabilities of transisions to temporary states from temporary states:'
    print S

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
        O[l,:] = O[l,:]/s
        l = l+1

    print 'Probabilities of transisions to particular terminal states:'
    print O

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

print solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
#print solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
#print solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
