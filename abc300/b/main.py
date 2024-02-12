import sys 
h, w = map(int, input().split())
a_ij = [input() for _ in range(h)]
b_ij = [input() for _ in range(h)]
isSame = True
for i in range(h) :
    for j in range(w) :
        for k in range(h) :
            for l in range(w) :
                if a_ij[k][l] != b_ij[(i+k)%h][(j+l)%w] :
                    isSame = False
        if isSame : 
            print("Yes")
            exit()
print("Yes" if isSame else "No")

