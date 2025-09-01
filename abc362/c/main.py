#!/usr/bin/env python3
# def find_zero_sum(n, l_r):
#     dp = {0: []}
#     for i in range(n):
#         new_dp = {}
#         for s in dp:
#             for x in range(l_r[i][0], l_r[i][1] + 1):
#                 new_sum = s + x
#                 if new_sum not in new_dp:
#                     new_dp[new_sum] = dp[s] + [x]
#                     # 合計0を見つけたら即座に返す
#                     if new_sum == 0:
#                         print('Yes')
#                         print(*new_dp[new_sum])
#                         return
#         dp = new_dp

#     print('No')

# if __name__ == "__main__":
#     n = int(input())
#     l_r = [list(map(int, input().split())) for _ in range(n)]
#     find_zero_sum(n, l_r)
# #!/usr/bin/env python3

# def find_zero_sum(n, l_r):
#     dp = {0: []}
#     for i in range(n):
#         new_dp = {}
#         for s in dp:
#             for x in range(l_r[i][0], l_r[i][1] + 1):
#                 new_sum = s + x
#                 if new_sum not in new_dp:
#                     new_dp[new_sum] = dp[s] + [x]
#         dp = new_dp

#     if 0 in dp:
#         print('Yes')
#         print(*dp[0])
#     else:
#         print('No')

# if __name__ == "__main__":
#     n = int(input())
#     l_r = [list(map(int, input().split())) for _ in range(n)]
#     find_zero_sum(n, l_r)

n = int(input())
l_r = [list(map(int,input().split())) for _ in range(n)]
pl,mi,zero = [],[],[]
plL,plR,miL,miR = 0,0,0,0
for i in range(n) :
    if l_r[i][0] <= 0 <= l_r[i][1] :
        zero.append(l_r[i])
    elif l_r[i][0] > 0 :
        pl.append(l_r[i])
        plL += l_r[i][0]
        plR += l_r[i][1]
    else :
        mi.append(l_r[i])
        miL += l_r[i][0]
        miR += l_r[i][1]
x = []
# 負の列が大きいとき
if plR < -miL :
    tmp = plR + miL
    zeroL = sum([max(zero[i][0],0) for i in range(len(zero))])
    zeroR = sum([max(zero[i][1],0) for i in range(len(zero))])
    print(tmp, zeroL,zeroR)
    if zeroL <= -tmp <= zeroR :
        # TODO　ここに l_r[i][0]<= x[i] <= l_r[i][1] かつ　sum(x) = 0　となるようなxを構成したい
        for i in range(n) :
            if l_r[i] in pl :
                x.append(l_r[i][1])
            elif l_r[i] in mi :
                x.append(l_r[i][1])
            else :
                x.append(min(l_r[i][1],-tmp))
                tmp += min(l_r[i][1],-tmp)

# 正の列が大きいとき
elif -miR < plL :
    tmp = plL + miR
    zeroL = sum([min(zero[i][0],0) for i in range(len(zero))])
    zeroR = sum([min(zero[i][1],0) for i in range(len(zero))])
    print(tmp, zeroL,zeroR)
    if -zeroR <= tmp <= -zeroL :
        # TODO　ここに l_r[i][0]<= x[i] <= l_r[i][1] かつ　sum(x) = 0　となるようなxを構成したい
        for i in range(n) :
            if l_r[i] in pl :
                x.append(l_r[i][1])
            elif l_r[i] in mi :
                x.append(l_r[i][1])
            else :
                x.append(min(l_r[i][1],-tmp))
                tmp += min(l_r[i][1],-tmp)
else :
        # TODO　ここに l_r[i][0]<= x[i] <= l_r[i][1] かつ　sum(x) = 0　となるようなxを構成したい

if len(x) == 0 :
    print('No')
else :
    print('Yes')
    print(*x)

# print(mi)
# print(zero)
# print(pl)
# print(miL,miR)
# print(plL,plR)
