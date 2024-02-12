#!/usr/bin/env python3
n = int(input())
while n%2 == 0 :
    n = n//2
while n%3 == 0 :
    n = n//3
# print(n)
print('Yes' if n == 1 else 'No')