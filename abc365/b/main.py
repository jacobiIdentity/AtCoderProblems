#!/usr/bin/env python3
n = int(input())
a_n = list(enumerate(list(map(int,input().split()))))
a_n.sort(key=lambda x:-x[1])
# print(a_n)
print(a_n[1][0]+1)