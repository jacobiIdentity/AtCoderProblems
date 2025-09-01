#!/usr/bin/env python3
# n = int(input())
# h_n = list(map(int,input().split()))
# ans = [0]*n
# # key:高さ, value:位置(0基準　)
# d = {h_n[i]:i for i in range(n)} 
# for i in reversed(range(1,n+1)) :
#     # iは何階か
#     pos = d[i]-1
#     while pos > -1 :
#         if h_n[pos] > i :
#             ans[pos] += 1
#             break
#         else :
#             ans[pos] += 1
#             pos -= 1
#         # print(i,pos,ans)
# print(*ans)

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, idx, delta):
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx
    
    def query(self, idx):
        sum = 0
        while idx > 0:
            sum += self.tree[idx]
            idx -= idx & -idx
        return sum

n = int(input())
h_n = list(map(int, input().split()))
ans = [0] * n

# Fenwick Treeの初期化
fenwick = FenwickTree(n)

# ビルの高さとそのインデックスを保持
buildings = [(h_n[i], i) for i in range(n)]
buildings.sort(reverse=True)

# 高いビルから順に処理していく
for height, index in buildings:
    # 現在のビルより右側にあるビルの数をFenwick Treeを使って取得
    ans[index] = fenwick.query(index + 1)
    # Fenwick Treeに現在のビルを追加
    fenwick.update(index + 1, 1)

print(*ans)
