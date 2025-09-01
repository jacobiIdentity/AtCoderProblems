#!/usr/bin/env python3
def calc(s) :
    # s = input()
    n = len(s)
    r,l = n-1,n-1
    candidates =[(n,n,'')]
    while l>-1 :
        if s[r]!=s[l] :
            if r-l>1 :
                candidates.append((l+1,r,s[r]))
            r = l
            continue
        if l == 0 :
            if r-l>0 :
                candidates.append((l,r,s[r]))
            break
        l -= 1
    # print(candidates)
    ans = 0
    for i in range(1,len(candidates)) :
        l,r,ss = candidates[i][0],candidates[i][1],candidates[i][2]
        tmp = n-1-r
        if candidates[i-1][2]==ss :
            tmp = candidates[i-1][1]-r-1
        rr = r+1
        while rr<candidates[i-1][0] :
            if s[rr] == ss :
                tmp -= 1
            rr+=1
        ans += tmp
    print(ans)
import random
import string

random.seed(1)  # 再現性のため固定シード

test_cases = []
for _ in range(100):
    length = random.randint(3, 100)  # 3〜100文字のランダム長
    s = ''.join(random.choices(string.ascii_lowercase, k=length))
    test_cases.append(s)

# 表示（必要ならファイル出力などにも変更可能）
for i, case in enumerate(test_cases, 1):
    print(f"Test case {i}: {case}")
    calc(case)