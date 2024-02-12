#!/usr/bin/env python3
h,w = map(int ,input().split())
a_hw = [list(map(int ,input().split())) for _ in range(h)]
b_hw = [list(map(int ,input().split())) for _ in range(h)]
tmpAH = sorted([sorted(a_hw[i]) for i in range(h)])
tmpBH = sorted([sorted(b_hw[i]) for i in range(h)])
if tmpAH != tmpBH :
    print(tmpAH)
    print(tmpBH)
    print(-1)
    exit()
tmpAG = sorted([sorted([a_hw[i][j] for i in range(h)]) for j in range(w)])
tmpBG = sorted([sorted([b_hw[i][j] for i in range(h)]) for j in range(w)])
if tmpAG != tmpBG :
    print(tmpAG)
    print(tmpBG)
    print(-1)
    exit()
