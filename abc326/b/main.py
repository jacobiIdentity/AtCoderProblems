#!/usr/bin/env python3
n326s = set()
for i in range(1,10) :
    for j in range(10) :
        if i*j > 9 :
            break
        n326s.add(100*i + 10*j+ i*j)
n = int(input())
print(min(filter(lambda x:x >= n, n326s)))