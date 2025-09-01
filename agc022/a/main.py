#!/usr/bin/env python3
s = input()
ans = ''
if len(s) <26 :
    for i in range(26) :
        if s.count(chr(ord('a')+i)) == 0 :
            ans = s+chr(ord('a')+i)
            break
else :
    tmp = {ord(s[-1])}
    for i in reversed(range(1,26)) :
        if ord(s[i-1]) > ord(s[i]) :
            tmp.add(ord(s[i-1]))
        else :
            # print(i)
            candidate = 100000
            for ss in tmp :
                if ord(s[i-1]) < ss :
                    candidate = min(candidate,ss)
            ans = s[:i-1]+chr(candidate)
            break
if ans == '' : ans = -1
print(ans)