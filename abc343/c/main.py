#!/usr/bin/env python3
n = int(input())
ans, tmp = 1, 1

while tmp*tmp*tmp <= n :
    tmp_cubic = tmp*tmp*tmp
    isPalindromic = True
    for i in range(len(str(tmp_cubic))//2) :
        if str(tmp_cubic)[i] != str(tmp_cubic)[len(str(tmp_cubic))-1-i] :
            isPalindromic = False
    if isPalindromic :
        ans = tmp_cubic
    tmp += 1
print(ans)