#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
p_a_b = [list(map(int,input().split())) for _ in range(n)]
ans = []
for i in range(5000001) :
    tmp = i
    for j in range(n) :
        p,a,b = p_a_b[j][0],p_a_b[j][1],p_a_b[j][2]
        if tmp<=p : 
            tmp += a
        else :
            tmp = max(tmp-b,0)
    ans.append(tmp)
# print(ans)
q = int(input())
for _ in range(q) :
    x = int(input())
    if x>= 5000000 :
        print(ans[-1]-5000000+x)
    else :
        print(ans[x])
