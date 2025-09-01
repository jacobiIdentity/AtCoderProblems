#!/usr/bin/env python3
s = input()
lenS = len(s)
l,r=0,0
ans = []
while l<lenS and r<lenS :
    if s[r]=="L" :
        border = r
        while r<lenS and s[r]=="L":
            r += 1
        for _ in range(border-l-1):
            ans.append(0)
        if (max(border-l,r-border)-1)%2==0 :
            if border-l <= r-border :
                ans.append((r-l)//2)
                ans.append((r-l)//2+(r-l)%2)
            else :
                ans.append((r-l)//2+(r-l)%2)
                ans.append((r-l)//2)
        else :
            if border-l <= r-border :
                ans.append((r-l)//2+(r-l)%2)
                ans.append((r-l)//2)
            else :
                ans.append((r-l)//2)
                ans.append((r-l)//2+(r-l)%2)
        for _ in range(r-border-1) :
            ans.append(0)
        l = r
    r+=1
print(*ans)