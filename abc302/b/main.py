import sys
h, w  = map(int, input().split())
s_h = [input() for _ in range(h)]
for i in range(h) :
    for j in range(w-4) :
        if s_h[i][j:j+5] == 'snuke' :
            for k in range(1, 6) :
                print(i+1, j+k)
            exit()
for i in range(h) :
    for j in range(w-4) :
        if s_h[i][j:j+5] == 'ekuns' :
            for k in range(5, 0, -1) :
                print(i+1, j+k)
            exit()
for i in range(h-4) :
    for j in range(w) :
        if s_h[i][j]+s_h[i+1][j]+s_h[i+2][j]+s_h[i+3][j]+s_h[i+4][j] == 'snuke' :
            for k in range(1, 6) :
                print(i+k, j+1)
            exit()
for i in range(h-4) :
    for j in range(w) :
        if s_h[i][j]+s_h[i+1][j]+s_h[i+2][j]+s_h[i+3][j]+s_h[i+4][j] == 'ekuns' :
            for k in range(5, 0, -1) :
                print(i+k, j+1)
            exit()
for i in range(h-4) :
    for j in range(w-4) :
        if s_h[i][j]+s_h[i+1][j+1]+s_h[i+2][j+2]+s_h[i+3][j+3]+s_h[i+4][j+4] == 'snuke' :
            for k in range(1, 6) :
                print(i+k, j+k)
            exit()
for i in range(h-4) :
    for j in range(w-4) :
        if s_h[i][j]+s_h[i+1][j+1]+s_h[i+2][j+2]+s_h[i+3][j+3]+s_h[i+4][j+4] == 'ekuns' :
            for k in range(5, 0, -1) :
                print(i+k, j+k)
            exit()
for i in range(4, h) :
    for j in range(w-4) :
        if s_h[i][j]+s_h[i-1][j+1]+s_h[i-2][j+2]+s_h[i-3][j+3]+s_h[i-4][j+4] == 'snuke' :
            for k in range(5) :
                print(i+1-k, j+1+k)
            exit()
for i in range(4, h) :
    for j in range(w-4) :
        if s_h[i][j]+s_h[i-1][j+1]+s_h[i-2][j+2]+s_h[i-3][j+3]+s_h[i-4][j+4] == 'ekuns' :
            for k in range(4, -1, -1) :
                print(i+1-k, j+1+k)
            exit()
