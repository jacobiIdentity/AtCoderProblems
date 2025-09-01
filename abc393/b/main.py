#!/usr/bin/env python3
s = input()
ans = 0
for i in range(len(s)-2) :
    for j in range(1,len(s)) :
        if i+j+j > len(s)-1 :
            break
        if s[i] == 'A' and s[i+j] == 'B' and s[i+2*j] == 'C': 
            ans += 1
            # print(i+1,i+j+1,i+j+j+1)
print(ans)
