#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
b_n = list(map(int,input().split()))
ans1 = 0
for i in range(n) :
    if a_n[i] == b_n[i] : ans1 += 1
print(ans1)
print(len(set(a_n)&set(b_n))-ans1)