#!/usr/bin/env python3
s = list(input())
ans = []
for i in range(len(s))  :
    if len(ans) == 0 :
        ans.append(s[i])
    elif ans[-1] == 'W' and s[i]== 'A' :
        ans.pop()
        tmp = []
        tmp.append('C')
        tmp.append('A')
        while len(ans) > 0 :
            t = ans.pop()
            if t == 'W' :
                tmp.pop()
                tmp.append('C')
                tmp.append('A')
            else :
                ans.append(t)
                break
        while len(tmp) > 0 :
            ans.append(tmp.pop())
    else :
        ans.append(s[i])
print(''.join(ans))
