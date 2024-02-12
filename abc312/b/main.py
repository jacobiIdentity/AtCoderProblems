#!/usr/bin/env python3
n, m = map(int, input().split())
s_n = ['+'*(m+1)]+['+'+input() for _ in range(n)]
for i in range(1, n+1) :
    if i+8 > n :
        # print('i: '+str(i))
        break
    for j in range(1, m+1) :
        isTak = True
        if j+8 > m :
            # print('j: '+str(j))
            break
        b = 0
        for k in range(9) :
            for l in range(9) :
                if (k < 3 and l < 3) or (k>5 and l>5) :
                    if s_n[i+k][j+l] == '.' :
                        isTak = False
                        break
                if (k == 3 and l < 4) or (k < 4 and l == 3) or (k == 5 and l > 4) or (k > 4 and l == 5):
                    if s_n[i+k][j+l] == '#' :
                        isTak = False
                        break
        if isTak :
            print(i,j)


                