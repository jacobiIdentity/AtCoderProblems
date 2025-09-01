#!/usr/bin/env python3
t = int(input())
for _ in range(t) :
    n = int(input())
    s = list(input())
    tmp = []
    l,r = 0,-1
    while l < n :
        if l == n-1 :
            tmp.append(s[l])
            break
        if s[l] <= s[l+1] :
            tmp.append(s[l])
            l += 1
            continue
        r = l
        while r < n+1 :
            if r==n :
                for j in range(l+1,n) :
                    tmp.append(s[j])
                tmp.append(s[l])
                l = r
                break
            if s[l]<s[r] :
                for j in range(l+1,r) :
                    tmp.append(s[j])
                tmp.append(s[l])
                for j in range(r,n) :
                    tmp.append(s[j])
                l = n
                break
            r+=1
    print("".join(tmp))

