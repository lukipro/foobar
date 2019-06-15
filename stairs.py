#!/usr/local/bin/python2

def stairs_ok(s):
    prev_step_count = s[0]+1
    for step_count in s:
        if prev_step_count <= step_count:
            return False
        prev_step_count = step_count
    return True


def create_stairs(n, stairs):
    #print 'creating stairs for n: ' + str(n)
    stairs[n] = set()
    for t in stairs[n-1]:
        cand = list(t)
        for i in range(len(cand)):
            candd = cand[:]
            candd[i] = candd[i]+ 1
      #      print 'candidate: ' + str(candd)
            if stairs_ok(candd):
    #            print 'stairs ok'
                stairs[n].add(tuple(candd))
        candd = cand[:]
        candd.append(1)
    #    print 'candidate: ' + str(candd)
        if stairs_ok(candd):
    #        print 'stairs ok'
            stairs[n].add(tuple(candd))

def solution(n):
    stairs = {3: {tuple([2,1])}}
    for i in range(3, n):
        create_stairs(i+1, stairs)

    print stairs[n]
    return len(stairs[n])

print solution(100)
