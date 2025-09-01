#!/usr/bin/env python3
n,c,k = map(int,input().split())
t_n = [int(input()) for _ in range(n)]
t_n.sort()
l,r=0,0
ans = 0
while r<n:
    if t_n[r]>t_n[l]+k :
        # print(l,r,r-l+1,t_n[r]-t_n[l])
        ans += 1
        # print(l,r,ans)
        l = min(l+c,r)
    elif r-l+1>c :
        # print(l,r,r-l+1,t_n[r]-t_n[l])
        ans += 1
        # print(l,r,ans)
        l += c
    if r==n-1:
        ans += (r-l+1)//c + (1 if (r-l+1)%c>0 else 0)
        # print(l,r,ans)
        break
    else :
        r += 1
# print(l,r)
print(ans)