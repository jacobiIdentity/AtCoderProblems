#!/usr/bin/env python3
n = int(input())
a_n = list(map(int, input().split()))
d = {a_n[i]-1:i for i in range(n)}
ans = []
for i in range(n) :
    if a_n[i] == i+1 :
        continue
    ans.append((i+1,d[i]+1))
    tmpdi,tmpdai = d[i], a_n[i]-1
    a_n[i], a_n[d[i]] = a_n[d[i]], a_n[i]
    d[i], d[tmpdai] = i, tmpdi
    # d[i], d[a_n[i]-1] = i, d[i]
    # a_n[i], a_n[d[i]], d[i], d[a_n[i]-1] = a_n[d[i]], a_n[i], i, d[i]
print(len(ans))
for i in range(len(ans)) :
    print(ans[i][0], ans[i][1])