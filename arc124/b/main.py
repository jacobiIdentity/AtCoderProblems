#!/usr/bin/env python3
n = int(input())
a_n = list(map(int, input().split()))
b_n = list(map(int, input().split()))
b_n.sort()

ans = []
candidates = [a_n[0] ^ b_n[j] for j in range(n)]

for candidate in candidates:
    transformed = sorted([candidate ^ a_n[i] for i in range(n)])
    if transformed == b_n:
        ans.append(candidate)

ans = sorted(set(ans))
print(len(ans))
print(*ans, sep="\n")
