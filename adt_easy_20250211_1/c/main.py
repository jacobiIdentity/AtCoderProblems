#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
ans = [a_n[0]]
for i in range(1,n) :
    if abs(ans[-1]-a_n[i]) < 2 :
        ans.append(a_n[i])
    elif ans[-1] < a_n[i] :
        ans += list(range(ans[-1]+1,a_n[i]+1))
    else :
        ans += list(reversed(range(a_n[i],ans[-1])))
print(*ans)
