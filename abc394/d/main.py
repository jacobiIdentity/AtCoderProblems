#!/usr/bin/env python3
s = list(input())
ans = []
for i in range(len(s))  :
    if len(ans) == 0 :
        ans.append(s[i])
    elif (ans[-1] == '(' and s[i]== ')') \
       or(ans[-1] == '[' and s[i]== ']') \
       or(ans[-1] == '<' and s[i]== '>') :
        ans.pop()
    else :
        ans.append(s[i])
print('Yes' if len(ans)==0 else 'No')
