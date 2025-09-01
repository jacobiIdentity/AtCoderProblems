#!/usr/bin/env python3
h,w,k = map(int,input().split())
grid = [input() for _ in range(h)]
ans = float('inf')
for i in range(h) :
    stt,cost,stp = 0,0,0
    isNG = False
    for stt in range(w-k+1) :
        while stt+stp < w :
            # 「x」: xの奥から探す
            if grid[i][stt+stp] == 'x' :
                if stp == k :
                    ans = min(ans,cost)
                isNG = True
                stp = 0
                cost = 0
                break
            # 「.」: cost 追加
            if grid[i][stt+stp] == '.' :
                cost += 1
            # kの時、最小値更新かどうか判断
            if stp+1 == k :
                ans = min(ans,cost)
                if grid[i][stt] == '.' :
                    cost -= 1
                stt += 1
                stp -= 1
            stp += 1
for j in range(w) :
    stt,cost,stp = 0,0,0
    while stt < h-k+1 :
        while stt+stp < h :
            # 「x」: xの奥から探す
            if grid[stt+stp][j] == 'x' :
                if stp == k :
                    ans = min(ans,cost)
                stt += stp+1
                stp = 0
                cost = 0
                break
            # 「.」: cost 追加
            if grid[stt+stp][j] == '.' :
                cost += 1
            # kの時、最小値更新かどうか判断
            if stp+1 == k :
                ans = min(ans,cost)
                if grid[stt+stp][j] == '.' :
                    cost -= 1
                stt += 1
                stp -= 1
            stp += 1
if ans == float('inf') :
    ans = -1
print(ans)