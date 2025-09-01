#!/usr/bin/env python3
n = int(input())

# エラトステネスの篩
def prime(x):
    is_prime = [True] * (x + 1)
    is_prime[0], is_prime[1] = False, False
    i = 2
    while i*i <= x :
        if is_prime[i]:
            for j in range(2 * i, x + 1, i):
                is_prime[j] = False
        i+=1
    return is_prime

# M以下の整数の素数判定
y = min(n,2*(10**6))
thieves = prime(y)

# 素数判定を基に, 素数リストを作成
prime_list = []
for i in range(y + 1):
    if thieves[i]:
        prime_list.append(i)
        
# print(*prime_list)
ans = set()
for p in prime_list :
    tmp = p
    tmp *= tmp
    tmp *= tmp
    tmp *= tmp
    if tmp > n :
        break
    ans.add(tmp)
for i in range(len(prime_list)) :
    pi = prime_list[i]
    if pi*pi*pi*pi > n :
        break
    for j in range(i+1,len(prime_list)) :
        pj = prime_list[j]
        if pi*pi*pj*pj > n :
            break
        ans.add(pi*pi*pj*pj)
print(len(ans))