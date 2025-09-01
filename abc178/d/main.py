#!/usr/bin/env python3
import math
s = int(input())
ans = 0
# comb = 1
for i in range(1,s//3+1) :
    ans += math.comb(s-2*i-1,i-1)
    # ans += comb
    ans %= 10**9+7
    # comb *= ((s-3*(i+1)-2)*(s-3*(i+1)-1)*(s-3*(i+1)))//((s-2*(i+1)-2)*(s-2*(i+1)-1)*(i+1))
    # comb %= 10**9+7
    # print(i,comb,ans)
# ans += comb
# ans %= 10**9+7
print(ans)