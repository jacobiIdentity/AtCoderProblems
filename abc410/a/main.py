#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
k = int(input())
print(len([]+list(filter(lambda x : x>=k,a_n))))