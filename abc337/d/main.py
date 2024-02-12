#!/usr/bin/env python3
h,w,k = map(int,input().split())
grid = [input() for _ in range(h)]
ans = max(h,w)+1
for i in range(h) :
    stt,length,cnt = -1,0,0
    for j in range(w) :
        if grid[i][j] == 'x' :
            stt,length,cnt = -1,0,0
        elif stt == -1 :
            stt,length = j,1
            cnt = 1 if grid[i][j] == '.' else 0
        else :
            length += 1
            cnt += 1 if grid[i][j] == '.' else 0
        if length == k :
            ans = min(ans, cnt)
            cnt -= 1 if grid[i][j-stt] == '.' else 0
            if k == 1 :
                stt = -1
            else :
                stt += 1
            length -= 1
for j in range(w) :
    stt,length,cnt = -1,0,0
    for i in range(h) :
        if grid[i][j] == 'x' :
            stt,length,cnt = -1,0,0
        elif stt == -1 :
            stt,length = i,1
            cnt = 1 if grid[i][j] == '.' else 0
        else :
            length += 1
            cnt += 1 if grid[i][j] == '.' else 0
        if length == k :
            # print(stt,length,cnt,ans)
            ans = min(ans, cnt)
            cnt -= 1 if grid[i-stt][j] == '.' else 0
            if k == 1 :
                stt = -1
            else :
                stt += 1
            length -= 1
    # print(stt,length,cnt)

print(ans if ans < max(h,w)+1 else -1)
            