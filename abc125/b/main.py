#!/usr/bin/env python3
n = int(input())
v_n = list(map(int,input().split()))
c_n = list(map(int,input().split()))
ans = 0
for i in range(n) :
    ans += (v_n[i]-c_n[i]) if v_n[i]-c_n[i]>0 else 0
# for i in range(1<<n) :
#     tmp = 0
#     for j in range(n) :
#         if i&(1<<j)==0 :
#             tmp += v_n[j]-c_n[j]
#     ans = max(ans,tmp)
print(ans)