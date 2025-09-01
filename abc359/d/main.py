#!/usr/bin/env python3
def is_palindrome(s):
    return s == s[::-1]

def count_good_strings(n, k, s):
    mod = 10**9 + 7  # 大きな数の場合のオーバーフロー対策
    
    # dp[i][j]: i番目まででjの状態のときの数
    dp = [[0] * (1 << k) for _ in range(n+1)]
    dp[0][0] = 1

    for i in range(n):
        for mask in range(1 << k):
            if dp[i][mask] == 0:
                continue
            for c in 'AB':
                new_mask = ((mask << 1) & ((1 << k) - 1)) | (c == 'B')
                if i >= k-1 and is_palindrome(s[max(0, i-k+1):i+1].replace('?', c)):
                    continue
                if s[i] == '?' or s[i] == c:
                    dp[i+1][new_mask] = (dp[i+1][new_mask] + dp[i][mask]) % mod
    
    return sum(dp[n]) % mod

# 入力
n, k = map(int, input().split())
s = input().strip()

# 出力
print(count_good_strings(n, k, s))
