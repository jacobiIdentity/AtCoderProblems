#!/usr/bin/env python3
n = int(input())
s_n = [input() for _ in range(n)]
l = max([len(s_n[i])for i in range(n)])
d = {n-i-1:max([len(s_n[j]) for j in range(i+1)]) for i in range(n)}
# print(d)
# print(l)
for i in range(l) :
    tmp = ''
    for j in range(n) :
        if i > d[j]-1 : break
        tmp += '*' if len(s_n[n-j-1])-1<i else s_n[n-j-1][i]
    print(tmp)
