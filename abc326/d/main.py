#!/usr/bin/env python3
n = int(input())
r = input()
c = input()
abc = 'ABC'
if not ('A' in r and 'B' in r and 'C' in r and \
        'A' in c and 'B' in c and 'C' in c) :
    print('No')
    exit()
ans = ['']*n
if n == 3 :
    ans[0] = c
    if r[0] != c[0] :
        print('No')
        exit()
    for i in range(1, n) :
        ans[i] = r[i]
        if ans[i][0] != ans[0][1] :
            for l in abc :
                if l not in ans[i][0]+ans[0][1] :
                    for m in abc :
                        if m not in ans[i][0]+l :
                            ans[i] += l+m
        else :
            for m in abc :
                if m not in ans[i][0]+ans[0][2] :
                    for l in abc :
                        if l not in ans[i][0]+m :
                            ans[i] += l+m
    print('Yes')
    for i in range(n) :
        print(ans[i])