#!/usr/bin/env python3
x = int(input())
print(x//10 if x%10==0 else ((x-x%10)//10+1))