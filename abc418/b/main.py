#!/usr/bin/env python3
s = input()
n = len(s)
ans = 0
for i in range(n-2) :
    if s[i] != "t" :
        continue
    for j in range(i+2,n) :
        if s[j]=="t" :
            ans = max(ans,(s[i:j+1].count("t")-2)/(j-i+1-2))
print('{:.14f}'.format(ans))