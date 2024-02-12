#!/usr/bin/env python3
import itertools
c_ij = list(map(int, input().split())) \
      +list(map(int, input().split())) \
      +list(map(int, input().split()))
p9s = list(itertools.permutations(range(9)))
rDict = dict()
rDict[0] = [0,3,6]
rDict[1] = [1,3]
rDict[2] = [2,3,7]
rDict[3] = [0,4]
rDict[4] = [1,4,6,7]
rDict[5] = [2,4]
rDict[6] = [0,5,7]
rDict[7] = [1,5]
rDict[8] = [2,5,6]
times = 0
for p9 in p9s :
    rows = [[] for _ in range(8)]
    isOK = True
    for pos in p9 :
        for r in rDict[pos] :
            if len(rows[r]) == 1 and c_ij[pos] in rows[r]:
                isOK = False
                # print(p9,pos,c_ij[pos], r, rows[r])
                break
            rows[r].append(c_ij[pos])
        if not(isOK) :
            break
    if isOK :
        # print(p9)
        times += 1
# print(times)
print('{:.20f}'.format(times/(9*8*7*6*5*4*3*2)) )
