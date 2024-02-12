#!/usr/bin/env python3
import sys
n, m = map(int, input().split())
pcf = []
for _ in range(n) :
    i = list(map(int, input().split()))
    p, c, f = i[0], i[1], set(i[2:])
    pcf.append((p,f))
for i in range(n) :
    for j in range(i, n) :
        if pcf[i][0] >= pcf[j][0] and pcf[i][1] < pcf[j][1] :
            print('Yes')
            exit()
        if pcf[i][0] > pcf[j][0] and pcf[i][1] <= pcf[j][1] :
            print('Yes')
            exit()
        if pcf[i][0] <= pcf[j][0] and pcf[i][1] > pcf[j][1] :
            print('Yes')
            exit()
        if pcf[i][0] < pcf[j][0] and pcf[i][1] >= pcf[j][1] :
            print('Yes')
            exit()
print('No')
