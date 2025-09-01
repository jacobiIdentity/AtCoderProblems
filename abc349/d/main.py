#!/usr/bin/env python3
l,r = map(int,input().split())
ans = []
while l <= r :
    ans.append(l)
    pow2, tmp = 1, l
    while tmp%2 == 0 and l+pow2*2 <= r :
        pow2 *= 2
        tmp //= 2
    l += pow2
    # print(l)
print(len(ans)-1)
for i in range(len(ans)-1) :
    print(ans[i],ans[i+1])
# print(ans)