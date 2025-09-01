#!/usr/bin/env python3
n = int(input())
s = input()
ans = 0
if n > 2 :
    for i in range(n-2) :
        if s[i]=='#'and s[i+2]=='#' and s[i+1]=='.' :
            ans += 1
print(0)
