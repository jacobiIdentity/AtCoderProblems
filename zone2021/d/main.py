#!/usr/bin/env python3
s = input().split('R')
s1 = ''.join([s[i] for i in range(1,len(s),2)])
s0 = ''.join([s[i] for i in range(0,len(s),2)])
tmp = s0[::-1]+s1
lMax = len(tmp)
next={i:i+1 for i in range(-1,lMax)}
prev={i:i-1 for i in range(lMax+1)}
i = 0
while i in next and next[i] in next :
    if tmp[i] == tmp[next[i]] :
        next[prev[i]] = next[next[i]]
        prev[next[next[i]]] = prev[i]
        if prev[i] != -1 :
            i = prev[i]
        elif next[next[i]] != lMax :
            i = next[next[i]]
        else :
            break
    else :
        i = next[i]
# ans = ''
ans = []
# print(prev)
# print(next)
if len(s)%2 :
    i = lMax
    while True :
        i = prev[i]
        if i == -1 :
            break
        # ans += tmp[i]
        ans.append(tmp[i])
else :
    i = -1
    while True :
        i = next[i]
        if i == lMax :
            break
        # ans += tmp[i]
        ans.append(tmp[i])
# if len(s)%2 :
#     ans = ans[::-1]
# print(ans)
print("".join(ans))