#!/usr/bin/env python3
n = int(input())
q_n = list(map(int, input().split()))
a_n = list(map(int, input().split()))
b_n = list(map(int, input().split()))
ans = 0
aMaxTmp = min([q_n[i]//a_n[i] if a_n[i] != 0 else 10**7 for i in range(n)])
for x in range(aMaxTmp+1) :
    ans = max(x+max(0,min([(q_n[i]-a_n[i]*x)//b_n[i] if b_n[i] != 0 else 10**7 for i in range(n)])),ans)
print(ans)