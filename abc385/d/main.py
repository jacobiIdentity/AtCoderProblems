#!/usr/bin/env python3
from collections import defaultdict
import bisect
n,m,x,y = map(int,input().split())
x_ys = [list(map(int,input().split())) for _ in range(n)]
d_c = [input().split() for _ in range(m)]
d_x = defaultdict(list)
d_y = defaultdict(list)
d_x_set = defaultdict(set)
d_y_set = defaultdict(set)
ans = set()
for i in range(n) :
    d_x[x_ys[i][0]].append(x_ys[i][1])
    d_y[x_ys[i][1]].append(x_ys[i][0])
    d_x_set[x_ys[i][0]].add(x_ys[i][1])
    d_y_set[x_ys[i][1]].add(x_ys[i][0])
for dd in d_x :
    d_x[dd].sort()
for dd in d_y :
    d_y[dd].sort()
for i in range(m) :
    c = int(d_c[i][1])
    st,ed = 0,0
    fst,lst = 0,0
    dlist,dset = 0,0
    if d_c[i][0] == 'U' :
        dlist = d_x
        dset = d_x_set
        fst,lst = y,y+c
        if x in d_x and not(lst < dlist[x][0] or fst > dlist[x][-1]) :
            st = bisect.bisect_left(dlist[x],fst)
            ed = bisect.bisect_left(dlist[x],lst)
            for j in range(st,ed) :
                ans.add((x,dlist[x][j]))
            if lst in dset[x] :
                ans.add((x,lst))
        y = lst
    if d_c[i][0] == 'D' :
        dlist = d_x
        dset = d_x_set
        fst,lst = y-c,y
        if x in d_x and not(lst < dlist[x][0] or fst > dlist[x][-1]) :
            st = bisect.bisect_left(dlist[x],fst)
            ed = bisect.bisect_left(dlist[x],lst)
            for j in range(st,ed) :
                ans.add((x,dlist[x][j]))
            if lst in dset[x] :
                ans.add((x,lst))
        y = fst
    if d_c[i][0] == 'R' :
        dlist = d_y
        dset = d_y_set
        fst,lst = x,x+c
        if x in d_y and not(lst < dlist[y][0] or fst > dlist[y][-1]) :
            st = bisect.bisect_left(dlist[y],fst)
            ed = bisect.bisect_left(dlist[y],lst)
            for j in range(st,ed) :
                ans.add((dlist[y][j],y))
            if lst in dset[y] :
                ans.add((lst,y))
        x = lst
    if d_c[i][0] == 'L' :
        dlist = d_y
        dset = d_y_set
        fst,lst = x-c,x
        if x in d_y and not(lst < dlist[y][0] or fst > dlist[y][-1]) :
            st = bisect.bisect_left(dlist[y],fst)
            ed = bisect.bisect_left(dlist[y],lst)
            for j in range(st,ed) :
                ans.add((dlist[y][j],y))
            if lst in dset[y] :
                ans.add((lst,y))
        x = fst
    # elif d_c[i][0] == 'D' :
    #     if x in d_x :
    #         if y < d_x[x][0] or y-c > d_x[x][-1] :
    #             y -= c
    #             continue
    #         st,ed = 0,0
    #         st = bisect.bisect_left(d_x[x],y-c)
    #         ed = bisect.bisect_left(d_x[x],y)
    #         for j in range(st,ed) :
    #             ans.add((x,d_x[x][j]))
    #         if y+c in d_x_set[x] :
    #             ans.add((x,y+c))
    #     y -= c
print(x,y,len(ans))