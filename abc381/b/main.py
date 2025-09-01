#!/usr/bin/env python3
s = input()
if len(s)%2==1 :
    print('No')
    exit()
ans = 'Yes'
used = set()
for i in range(len(s)//2) :
    if s[2*i] != s[2*i+1] :
        ans = 'No'
        break
    elif s[2*i] in used :
        ans = 'No'
        break
    else :
        used.add(s[2*i])
print(ans)