import sys
x, y, z = map(int, input().split())
s = input()
dp = [0]*(len(s)+1)
isUs = [False]*(len(s)+1)
for i in range(n) :
    