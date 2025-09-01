#!/usr/bin/env python3
import itertools
n = int(input())
s = input()
s_n2 = [int(s[i])*(i+1) for i in range(n)]
acc2 = list(itertools.accumulate(s_n2))
acc2.reverse()
# print(*acc2)
ans = ''
# 繰り上がり用変数
carry = 0 
for i in range(n) :
    tmp = carry + acc2[i]
    ans = str(tmp%10)+ans
    carry = tmp//10
if carry > 0 :
    ans = str(carry)+ans
print(ans)
