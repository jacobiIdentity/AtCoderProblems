#!/usr/bin/env python3
# n,m,k = map(int,input().split())
# c_a_ij_r = [list(map(int,input().split())) for _ in range(m)]

# for i in range(n) :
#     tmp = i+1
#     if l <= i+1 <= r :
#         tmp = r + l - i-1
#     if i != n-1 :
#         print(tmp, end=" ")
#     else :
#         print(tmp)
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    M = int(data[1])
    K = int(data[2])

    tests = []
    index = 3
    for _ in range(M):
        Ci = int(data[index])
        Ai = list(map(int, data[index+1:index+1+Ci]))
        Ri = data[index+1+Ci]
        tests.append((Ai, Ri))
        index = index + 1 + Ci + 1

    # dp[mask] = True if the combination represented by mask is valid
    dp = [True] * (1 << N)

    # Process each test
    for Ai, Ri in tests:
        new_dp = [False] * (1 << N)
        for mask in range(1 << N):
            if not dp[mask]:
                continue

            # Count the number of correct keys in Ai
            correct_keys = sum(1 for key in Ai if (mask & (1 << (key - 1))) != 0)
            
            if (Ri == 'o' and correct_keys >= K) or (Ri == 'x' and correct_keys < K):
                new_dp[mask] = True
        
        dp = new_dp

    # Count the number of valid masks
    valid_combinations = sum(dp)
    print(valid_combinations)

solve()