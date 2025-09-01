#!/usr/bin/env python3
from collections import deque
h,w = map(int, input().split())
s = [input() for _ in range(h)]
ans = 0
# 上下左右の移動方向を定義
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 各マスの自由度を計算する
for i in range(h):
    for j in range(w):
        visited = [[False] * w for _ in range(h)]
        if s[i][j] == '.':
            visited[i][j] = True
            queue = deque([(i, j)])
            freedom = 1  # 自分自身も含める
            while queue:
                x, y = queue.popleft()
                isNextToMag = False
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < h and 0 <= ny < w and s[nx][ny] == '#' :
                        isNextToMag = True
                        break
                if isNextToMag : continue
                
                # if (0 <= x-1 < h and s[x-1][y] != '#') or (0 <= x+1 < h and s[x+1][y] != '#') \
                #    or (0 <= y-1 < w and s[x][y-1] != '#') or (0 <= y+1 < w and s[x][y+1] != '#'):
                #     continue
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < h and 0 <= ny < w and s[nx][ny] == '.' and not visited[nx][ny] :
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        freedom += 1

            ans = max(ans, freedom)

print(ans)