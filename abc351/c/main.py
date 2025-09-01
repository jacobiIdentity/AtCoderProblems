#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
ans = []
for i in range(n) :
    ans.append(a_n[i])
    while len(ans) > 1 :
        if ans[-1] == ans[-2] :
            last = ans.pop(-1) +1
            ans.pop(-1)
            ans.append(last)
        else :
            break
print(len(ans))