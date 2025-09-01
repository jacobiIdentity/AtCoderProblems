#!/usr/bin/env python3
def rps(takahashi,aoki) :
    if takahashi == aoki:
        return 0
    if takahashi == 0 and aoki == 1 :
        return -1
    if takahashi == 0 and aoki == 2 :
        return 1
    if takahashi == 1 and aoki == 2 :
        return -1
    if takahashi == 1 and aoki == 0 :
        return 1
    if takahashi == 2 and aoki == 1 :
        return 1
    if takahashi == 2 and aoki == 0 :
        return -1
n = int(input())
s = input()
dp2 = [[0]*3 for i in range(n+1)]
for i in range(n+1) :
    a = 0 if s[i-1]=='R' else (1 if s[i-1]=='P' else 2)
    if i == 0 : continue
    for j in range(3) :
        # 負けの場合は-1
        if rps(j,a) == -1 :
            dp2[i][j] = -1
            continue
        for k in range(3) :
            if k == j : continue
            if dp2[i-1][k] != -1 :
                dp2[i][j] = max(dp2[i-1][k]+rps(j,a),dp2[i][j])
print(max(dp2[-1]))
# print(dp2)

# dp = [[0]*3 for i in range(n+1)]
# for i in range(n+1) :
#     for j in range(3) :
#         if i == 0 :
#             dp[i][j] == 0
#             break
#         a = 0 if s[i-1]=='R' else (1 if s[i-1]=='P' else 2)
#         if j == 0 :
#             if a==1 :
#                 dp[i][j] = -1
#                 continue
#             if dp[i-1][1] != -1 :
#                 dp[i][j] = dp[i-1][1]+rps(j,a)
#             if dp[i-1][2] != -1 :
#                 dp[i][j] = max(dp[i-1][2]+rps(j,a),dp[i][j])
#         elif j == 1 :
#             if a==2 :
#                 dp[i][j] = -1
#                 continue
#             if dp[i-1][2] != -1 :
#                 dp[i][j] = dp[i-1][2]+rps(j,a)
#             if dp[i-1][0] != -1 :
#                 dp[i][j] = max(dp[i-1][0]+rps(j,a),dp[i][j])
#         else :
#             if a==0 :
#                 dp[i][j] = -1
#                 continue
#             if dp[i-1][0] != -1 :
#                 dp[i][j] = dp[i-1][0]+rps(j,a)
#             if dp[i-1][1] != -1 :
#                 dp[i][j] = max(dp[i-1][1]+rps(j,a),dp[i][j])
# print(max(dp[-1]))

# print(dp)
        