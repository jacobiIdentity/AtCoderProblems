#!/usr/bin/env python3
s = input()
ls = len(s)
ans = 1
for i in range(1,ls+1) :
    for j in range(ls-i+1) :
        isPalindrome = True
        for k in range(i//2) :
            if s[j+k] != s[j+i-1-k] :
                # print(i,j,k,s[j+k],s[j+i-1-k])
                isPalindrome = False
                break
        if isPalindrome :
            ans = max(ans,i)
            break
print(ans)