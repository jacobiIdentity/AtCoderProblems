#!/usr/bin/env python3
import itertools
n,s = map(int,input().split())
a_n = list(map(int,input().split()))
sumA = sum(a_n)
s%= sumA
if s == 0 :
    print('Yes')
    exit()
a_n2 = a_n + a_n
l,r = 0,0
tmp = a_n[0]
while l <= r and r < 2*n :
    # print(l,r,tmp)
    if tmp == s :
        print('Yes')
        exit()
    if tmp < s :
        if r < 2*n-1 :
            r += 1
            tmp += a_n2[r]
        else :
            # n+1以降の場合もあるが、後で処理
            break
    elif tmp > s :
        if l < r :
            tmp -= a_n2[l]
            l += 1
        elif l == r and r < 2*n-1 :
            l+= 1
            r+= 1
            tmp = a_n2[l]
        else :
            break

# acm1 = set(itertools.accumulate(a_n))
# acm2 = set(itertools.accumulate(reversed(a_n)))
# for subSumA in acm2 :
#     if s-subSumA in acm1 :
#         print('Yes')
#         exit()
print('No')