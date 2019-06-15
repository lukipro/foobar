#!/usr/local/bin/python2
def stairs_ok(s):
    prev_step_count = s[0]+1
    for step_count in s:
        if prev_step_count <= step_count:
            return False
        prev_step_count = step_count
    return True


def create_stairs(n, stairs):
    stairs[n] = set()
    for t in stairs[n-1]:
        cand = list(t)
        for i in range(len(cand)):
            cand[i] = cand[i]+ 1
            if stairs_ok(cand):
                stairs[n].add(tuple(cand))
            cand[i] = cand[i]- 1
        cand.append(1)
        if stairs_ok(cand):
            stairs[n].add(tuple(cand))

def solution(n):
    stairs = {3: {tuple([2,1])}}
    for i in range(3, n):
        create_stairs(i+1, stairs)

    #print stairs[n]
    return len(stairs[n])

#print solution(200)
for n in range(4,100):
     print 'n: ' + str(n) + ' res: ' + str(solution(n))
