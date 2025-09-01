#!/usr/bin/env python3
import math
n = int(input())
p = 998244353
# 丸め誤差にやられた
# k = math.floor(math.log10(n))+1
k = len(str(n))
ans = n%p
ans *= (pow(10, k*n, mod=p)-1)
ans %= p
div = (pow(10, k, mod=p) -1)%p
div = pow(div, p-2, mod=p)
ans *= div
ans %= p
print(ans)

## ↑丸め誤差で1問通らなくて chatGPTさんに教えてもらった
# # 10^k % p
# power_10_k = pow(10, k, p)

# # (10^(k*n) - 1) % p
# numerator = (pow(10, k*n, p) - 1 + p) % p

# # (10^k - 1) % p の逆元を計算
# div = (power_10_k - 1 + p) % p
# inverse_div = pow(div, p - 2, p)

# # V_N % p を計算
# ans = n % p
# ans = ans * numerator % p
# ans = ans * inverse_div % p

## 下記簡易的な解法メモ
# 求める値をpで割る前の値
#  = n* ∑_(1<=i<=n)10^(k*(i-1))
#  = n*(10^kn -1)//(10^k -1)
#    合同式の世界では直接割り算はNG
#    分母の逆元を求め、それをansにかけることで解消する
#    つまり
#      x * (10^k-1)^(p -1) ≡ 1 (mod p)
#    となる pを算出する
#      今回 10^k-1 と p は copirme なので
#     フェルマーの小定理より
#       (10^k -1)^(p -2) * (10^k-1) ≡ (10^k-1)^(p -1) ≡ 1 (mod p)
#     よって 10^k -1 で割ることは (10^k -1)^(p -2) をかけることと等しい
