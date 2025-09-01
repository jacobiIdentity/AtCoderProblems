#!/usr/bin/env python3
a,b,c,d,e,f = map(int ,input().split())
g,h,i,j,k,l = map(int ,input().split())
isYes = False
# 2つ目の図形の頂点が1つ目の図形の内部かどうかチェック gとj、hとk、iとlの入れ替え
if a < g < d and b < h < e and c < i < f :
    isYes = True
if a < g < d and b < h < e and c < l < f :
    isYes = True
if a < g < d and b < k < e and c < i < f :
    isYes = True
if a < g < d and b < k < e and c < l < f :
    isYes = True
if a < j < d and b < h < e and c < i < f :
    isYes = True
if a < j < d and b < h < e and c < l < f :
    isYes = True
if a < j < d and b < k < e and c < i < f :
    isYes = True
if a < j < d and b < k < e and c < l < f :
    isYes = True
# 1つ目の図形の頂点が2つ目の図形の内部かどうかチェック aとd、bとe、cとfの入れ替え
if g < a < j and h < b < k and i < c < l :
    isYes = True
if g < a < j and h < b < k and i < f < l :
    isYes = True
if g < a < j and h < e < k and i < c < l :
    isYes = True
if g < a < j and h < e < k and i < f < l :
    isYes = True
if g < d < j and h < b < k and i < c < l :
    isYes = True
if g < d < j and h < b < k and i < f < l :
    isYes = True
if g < d < j and h < e < k and i < c < l :
    isYes = True
if g < d < j and h < e < k and i < f < l :
    isYes = True
# (g,h,i)がC(a,b,c,d,e,f)の辺上に存在
if a == g and b == h and c <= i < f :
    isYes = True
if a == g and b <= h < e and c == i :
    isYes = True
if a <= g < d and b == h and c == i :
    isYes = True
# (j,k,l)がC(a,b,c,d,e,f)の辺上に存在
if d == j and e == k and c < l <= f :
    isYes = True
if d == j and b < k <= e and f == l :
    isYes = True
if a < j <= d and e == k and f == l :
    isYes = True
# (a,b,c)がC(g,h,i,j,k,l)の辺上に存在
if a == g and b == h and i <= c < l :
    isYes = True
if a == g and h <= b < k and c == i :
    isYes = True
if g <= a < j and b == h and c == i :
    isYes = True
# (d,e,f)がC(g,h,i,j,k,l)の辺上に存在
if d == j and e == k and i < f <= l :
    isYes = True
if d == j and h < e <= k and f == l :
    isYes = True
if g < d <= j and e == k and f == l :
    isYes = True
print('Yes' if isYes else 'No')
