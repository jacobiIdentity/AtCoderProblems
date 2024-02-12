#!/usr/bin/env python3
h, w = map(int, input().split())
s_ij = [list(input()) for _ in range(h)]
cnt, fst, tgt = -1, w+1, w+1
for i in range(h) :
    t = s_ij[i].count('#') 
    if t > 0 :
        fst = i if fst > w else fst
        cnt = t if cnt < 0 else cnt
        if cnt < t :
            tgt = fst
            fst = i
            break
        elif cnt > t :
            tgt = i
            break
# print(fst, tgt)
for j in range(w) :
    if s_ij[fst][j] != s_ij[tgt][j] :
        print(tgt+1, j+1)
        break