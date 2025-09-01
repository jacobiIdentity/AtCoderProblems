#!/usr/bin/env python3
import bisect, itertools
n,m = map(int,input().split())
a_n = sorted(list(map(int,input().split())))
# if sum(a_n) <= m :
    # print('infinite')
    # exit()
cms = list(itertools.accumulate(a_n))
# cms = [0]+list(itertools.accumulate(a_n))
# for i in range(n+1) :
#     cms[n-i]+a_n[i-1]*i
left = m//n
right = 4*(10**14)+1
mid = 0
# print(a_n)
# print(cms)
while right - left > 1 :
    mid = (left+right)//2
    pos = bisect.bisect_right(a_n,mid)
    val = 0
    if pos == 0 :
        val = mid*n
    elif pos == n :
        val = sum(a_n)
        if val <= m :
            print('infinite')
            exit()
    else :
        val = cms[pos-1]+mid*(n-pos)
    # print(left,right,mid,pos,val)
    if val > m :
        right = mid
    else :
        left = mid
mid = (left+right)//2
print(mid if mid < m else 'infinite')
    

