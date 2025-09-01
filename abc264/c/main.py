#!/usr/bin/env python3
h1,w1 = map(int ,input().split())
a_ij = [input().split() for _ in range(h1)]
h2,w2 = map(int ,input().split())
b_ij = [input().split() for _ in range(h2)]
for i in range(1<<(h1+w1)) :
    bI = format(i,'0{}b'.format(h1+w1))
    if bI[:h1].count('1')+h2 == h1 and bI[h1:].count('1')+w2 == w1:
        isYes = True
        skipH = 0
        for i in range(h1) :
            if bI[i] == '1':
                skipH += 1
                continue
            skipW = 0
            for j in range(w1) :
                if bI[h1+j] == '1':
                    skipW += 1
                    continue
                if b_ij[i-skipH][j-skipW] != a_ij[i][j] :
                    isYes = False
                    # print(bI,skipH,skipW,'',i,j,'',i-skipH,j-skipW,'',b_ij[i-skipH][j-skipW],a_ij[i][j])
                    break
            if not(isYes) :
                break
        if isYes :
            break
print('Yes' if isYes else 'No') 

