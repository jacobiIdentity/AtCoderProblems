#!/usr/bin/env python3
n = int(input())
s = input()
ans = 1
i = 1
# while i < n :
for i in range(1,n-1) :
    if s[i-1]=='1' and s[i]=='/' and s[i+1]=='2' :
        k = 1
        while -1<i-k < i+k < n :
            if s[i-k] == '1' and s[i+k] == '2' :
                k += 1
            else :
                break
        # print(s[i-k:i+k+1])
        ans = max(ans,2*k-1)
        # i += k
    # else :
        # i += 1
print(ans)