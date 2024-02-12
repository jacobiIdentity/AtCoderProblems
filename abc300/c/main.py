import sys
def checkSize(x, y) :
    d = 0
    while d < min(h,w)//2 + 1 :
        if x+d > h or y+d > h or c_ij[x+d][y+d] != '#' :
            break
        if x+d > h or y-d < 0 or c_ij[x+d][y-d] != '#' :
            break
        if x-d < 0 or y+d > h or c_ij[x-d][y+d] != '#' :
            break
        if x-d < 0 or y-d < 0 or c_ij[x-d][y-d] != '#' :
            break
        d += 1
    ans[d-1] += 1
    return 

h, w = map(int, input().split())
c_ij = [input() for _ in range(h)]
centers = set()
ans = [0]*min(h, w)
for i in range(1, h-1) :
    for j in range(1, w-1) :
        if c_ij[i][j] != '#' :
            continue
        if c_ij[i+1][j+1] == '#' and c_ij[i+1][j-1] == '#' and c_ij[i-1][j+1] == '#' and c_ij[i-1][j-1] == '#':
            centers.add((i, j))
print(*ans)


