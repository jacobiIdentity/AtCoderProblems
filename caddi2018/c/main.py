#!/usr/bin/env python3
from collections import defaultdict
def getPrimes(x) :
    ret = set()
    thieves = [True]*(x+1)
    thieves[0],thieves[1]= False,False
    p = 2
    for p in range(2,x+1) :
        if not(thieves[p]) : continue
        ret.add(p)
        q = p+p
        while q < x+1 :
            thieves[q] = False
            q += p
        p+= 1
    return ret

n,p = map(int,input().split())
tmp = 1 
while tmp*tmp < p+1 :
    tmp += 1
ps = getPrimes(tmp)
ans = 1
# for i in range(2,tmp+1) :
#     if ps[i] :
#         cnt = 0
#         now = p
#         while now%i==0 :
#             now //= i
#             cnt += 1
#         ans *= i**(cnt//n)
# print(ans)
now = p
d = defaultdict(int)
for tmp in ps :
# while tmp*tmp < p+1 :
    # tmp += 1
    # cnt = 0
    while now%tmp == 0 :
        now //= tmp
        # cnt += 1
        d[tmp] += 1
    # ans *= tmp**(cnt//n)
    # if p%tmp == 0 :
    #     cnt = 0
    #     while now%(p//tmp)== 0 :
    #         now //= (p//tmp)
    #         cnt += 1
    #     ans *= (p//tmp)**(cnt//n)
# if n == 1 : ans =p
d[now] = 1
for dd in d :
    ans *= dd**(d[dd]//n)
print(ans)
