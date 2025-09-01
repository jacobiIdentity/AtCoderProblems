#!/usr/bin/env python3
def calcLCM(a,b) :
    x,y = a,b
    if x > y :
        x,y = y,x
    while x>0 :
        x,y = y%x,x
    return n*m//y
n,m,k = map(int, input().split())
lcm =calcLCM(n,m)
# a,b = n,m
# divs = []
# cnt,now = 0,0
# while cnt<(k-1)%(lcm//m+lcm//n-2)+1:
#     if a<b :
#         # divs.append(a)
#         now = a
#         a += n
#     else :
#         # divs.append(b)
#         now = b
#         b += m
#     cnt += 1
# # print(divs)
# # print(now)
# # print(lcm*((k-1)//(lcm//m+lcm//n-2))+divs[(k-1)%(lcm//m+lcm//n-2)])
# print(lcm*((k-1)//(lcm//m+lcm//n-2))+now)
ok,ng = 2*10**18,0
while ok-ng>1 :
    mid = (ok+ng)//2
    if mid//m+mid//n-2*(mid//lcm) >= k :
        ok = mid
    else :
        ng = mid
print(ok)