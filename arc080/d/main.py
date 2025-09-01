#!/usr/bin/env python3
h,w = map(int,input().split())
n = int(input())
a_n = list(map(int,input().split()))
a_n_withI = [(-a_n[i],i+1) for i in range(n)]
a_n_withI.sort()
# print(a_n_withI)
i,j = 0,0
nowColorPos = 0
cnt =0
ans = [[-1]*w for _ in range(h)]
while i<h and j<w :
    if cnt == -a_n_withI[nowColorPos][0] :
        nowColorPos += 1
        cnt=0
    # print(i,j,cnt,-a_n_withI[nowColorPos][0],a_n_withI[nowColorPos][1])
    ans[i][j] = a_n_withI[nowColorPos][1]
    cnt+=1
    if (w>1 and j==w-1 and ans[i][j-1]>-1) or (w>1 and j==0 and ans[i][j+1]>-1) or w==1:
        print(*ans[i],sep=" ")
        i+=1
    elif (0<=j-1<w and ans[i][j-1]==-1) :
        j-=1
    else :
        j+=1

