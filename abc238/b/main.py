#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
now = 0
angles = [0]
for i in range(n) :
    now += a_n[i]
    now %= 360
    angles.append(now)
angles.sort()
# print(angles)
angles.append(360)
print(max([angles[i+1]-angles[i] for i in range(len(angles)-1)]))