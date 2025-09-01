#!/usr/bin/env python3

n = int(input())
a_n = list(map(int,input().split()))
a_n_i = [(a_n[i],i) for i in range(n)]
a_n_i.sort()
d = {a_n_i[i][1]:i for i in range(n)}
for i in range(n):
    med = 0
    if d[i] < n//2 :
        med = n//2
    else :
        med = n//2-1
    print(a_n_i[med][0])
