#!/usr/bin/env python3
import itertools
n,k = map(int,input().split())
s = input()
sArr = [ss for ss in s]
print(len(sArr))
print(sArr)
ans = 0
for cmb in itertools.combinations(sArr,len(s)) :
    for i in range(n-k+1) :
        # if 2*i
        isPal = True
        for j in range(k) :
            if cmb[i+j-1]!= cmb[i+k+1-j+1] :
                isPal = False
                break
        if isPal :
            break
        ans += 1
print(ans)