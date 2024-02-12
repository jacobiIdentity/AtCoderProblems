import sys
n, m, d = map(int, input().split())
a_n = sorted(list(map(int, input().split())))
b_m = sorted(list(map(int, input().split())))
dp = [[-1]*(n+1) for _ in range(m+1)]
for i in range(1, n+1) :
    for j in range(1, m+1) :
