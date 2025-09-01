#!/usr/bin/env python3
n,m = map(int,input().split())
b_n = list(map(int,input().split()))
w_m = list(map(int,input().split()))
b_n.sort(key=lambda x:-x)
w_m.sort(key=lambda x:-x)
ans = 0
threshold = -1
for i in range(n) :
    if b_n[i] < 0 :
        threshold = i
        break
    else :
        ans += b_n[i]
# print(threshold)
if threshold == -1 :
    threshold = n
for i in range(m) :
    if i < threshold :
        if w_m[i] >= 0 :
            ans += w_m[i]
        else :
            break
    elif i < n and b_n[i]+w_m[i] >= 0 :
        ans += b_n[i]+w_m[i]
    # elif  w_m[i] >= 0 :
    #     ans += w_m[i]
    else :
        break

print(ans)            
