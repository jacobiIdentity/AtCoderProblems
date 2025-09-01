#!/usr/bin/env python3
n = int(input())
p_n = list(map(int,input().split()))
q_n = list(map(int,input().split()))
q_minus1 = {q_n[i]:i+1 for i in range(n)}
ans = [q_n[p_n[q_minus1[i]-1]-1] for i  in range(1,n+1)]
print(*ans)