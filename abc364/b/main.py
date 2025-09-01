#!/usr/bin/env python3
h,w = map(int,input().split())
s_i,s_j = map(int,input().split())
c_ij = [input() for _ in range(h)]
x = input()
now = s_i-1,s_j-1
for i in range(len(x)) :
    p,q = 0,0
    if x[i]== 'L' and now[1]>0 and c_ij[now[0]][now[1]-1]=='.' :
        q = -1
    elif x[i]== 'R' and now[1]<w-1 and c_ij[now[0]][now[1]+1]=='.' :
        q = 1
    elif x[i]== 'U' and now[0]>0 and c_ij[now[0]-1][now[1]]=='.' :
        p = -1
    elif x[i]== 'D' and now[0]<h-1 and c_ij[now[0]+1][now[1]]=='.' :
        p = 1
    now = now[0]+p,now[1]+q
print(now[0]+1,now[1]+1)