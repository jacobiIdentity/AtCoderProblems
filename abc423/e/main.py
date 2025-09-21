#!/usr/bin/env python3
n,q = map(int, input().split())
a_n = list(map(int, input().split()))

acs_a = [0]*(n+1)
acs_a_j = [0]*(n+1)
acs_a_j_j = [0]*(n+1)

for i in range(1, n+1):
    acs_a[i] = acs_a[i-1] + a_n[i-1]
    acs_a_j[i] = acs_a_j[i-1] + i*a_n[i-1]
    acs_a_j_j[i] = acs_a_j_j[i-1] + i*i*a_n[i-1]

for _ in range(q):
    l, r = map(int, input().split())
    sum_a = acs_a[r] - acs_a[l-1]
    sum_a_j = acs_a_j[r] - acs_a_j[l-1]
    sum_a_j_j = acs_a_j_j[r] - acs_a_j_j[l-1]
    ans = -sum_a_j_j + (r+l)*sum_a_j + (r+1)*(1-l)*sum_a
    print(ans)
