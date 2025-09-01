#!/usr/bin/env python3
import itertools,math
n,s,t = map(int,input().split())
dots = [list(map(int,input().split())) for _ in range(n)]
# print(dots)
ans = float('inf')
for i in range(1<<n) :
    iStr = ('{:0'+str(n)+'b}').format(i)
    for perms in itertools.permutations(list(range(n))) :
        # print(perms)
        startDot = (0,0)
        tmp = 0
        for j in perms :
            dot1,dot2 = (dots[j][0],dots[j][1]),(dots[j][2],dots[j][3])
            if iStr[j] == '1':
                dot1,dot2 = dot2,dot1
            tmp += math.sqrt((startDot[0]-dot1[0])**2+(startDot[1]-dot1[1])**2)/s
            tmp += math.sqrt((dot2[0]-dot1[0])**2+(dot2[1]-dot1[1])**2)/t
            startDot = (dot2[0],dot2[1])
            # print(i)
        ans = min(ans,tmp)    
print(ans)