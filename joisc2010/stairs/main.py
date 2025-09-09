#!/usr/bin/env python3
import sys, bisect
MOD = 1234567
input = sys.stdin.readline

n,p = map(int,input().split())
a = [0]+[int(input()) for _ in range(n)]

for i in range(1,n+1):
    a[i] += a[i-1]

dp = [0]*(n+1)
pref = [0]*(n+1)   # 累積和 dp[0..i]
dp[0] = 1
pref[0] = 1

for r in range(1,n+1):
    # L = 最小のインデックスで s[L] >= s[r]-p
    L = bisect.bisect_left(a, a[r]-p, 0, r)
    dp[r] = (pref[r-1] - (pref[L-1] if L>0 else 0)) % MOD
    pref[r] = (pref[r-1]+dp[r]) % MOD

print(dp[n])


# #!/usr/bin/env python3
# MOD = 1234567
# n,p = map(int,input().split())
# h_n = [0]+[int(input()) for _ in range(n)] +[0]
# for i in range(n+1) :
#     h_n[i+1] += h_n[i]
# print(h_n)
# dp = [0]*(n+1)
# dp[0] = 1
# for i in range(n) :
#     ok,ng = i,n+1
#     while ng-ok>1 :
#         mid = (ok+ng)//2
#         if h_n[mid]-h_n[i] <= p :
#             ok = mid
#         else :
#             ng = mid
#     # dp[i] += 2
#     # dp[ok+1]  -= 1
#     dp[ok]  += dp[i]*((ok-i)*(ok-i+1))//2
#     print(i,ok,h_n[ok]-h_n[i],dp)
#     # [1,_1,_1,_2,_3,_6,_9,_0]
#     # for j in range(i+1,n+1) :
#     #     if h_n[j]-h_n[i] <= p:
#     #         dp[j] += dp[i]
#     #         dp[j] %= MOD
#     #     else :
#     #         break
# print(dp)
# for i in range(n) :
#     dp[i+1] += dp[i]
# print(dp[-1])
# print(dp)