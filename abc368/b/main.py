#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
ans = 0
while len(a_n)> 1 :
    a_n.sort(reverse=True)
    a_n[0] -= 1
    a_n[1] -= 1
    ans += 1
    if a_n[1] < 1 :
        a_n.remove(a_n[1])
    if a_n[0] < 1 :
        a_n.remove(a_n[0])
print(ans)