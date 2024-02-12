import sys
n, m, h, k = map(int, input().split())
s = input()
items = {tuple(map(int, input().split())) for _ in range(m)}
hNow, xNow, yNow, cnt = h, 0, 0, 0
while hNow > -1 and cnt < n :
    hNow -= 1
    if s[cnt] == 'R' :
        xNow += 1
    if s[cnt] == 'L' :
        xNow -= 1
    if s[cnt] == 'U' :
        yNow += 1
    if s[cnt] == 'D' :
        yNow -= 1
    if hNow < 0 :
        print('No')
        exit()
    cnt += 1
    if (xNow, yNow) in items and hNow < k :
        hNow = k
        items.remove((xNow, yNow))
print('Yes' if hNow > -1 else 'No')