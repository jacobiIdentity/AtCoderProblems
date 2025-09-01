def is_possible(x):
    need = 0  # xにするためにaが必要な合計回数
    give = 0  # xより大きい値からbで減らして提供できる合計回数
    for i in range(n) :
        if a_n[i] < x:
            # val を x 以上にするには ceil((x - val) / a) 回 a を足す
            # a-1は床関数(切り上げ)のためのおまじない
            need += (x-a_n[i]+a-1)//a
        else:
            # val を x に落とすには (val - x) // b 回 b を減らせる
            give += (a_n[i]-x)//b
    return need <= give

n,a,b = map(int, input().split())
a_n = list(map(int, input().split()))

ok = min(a_n)
ng = max(a_n) + 1

while ng - ok > 1:
    mid = (ng + ok) // 2
    if is_possible(mid):
        ok = mid
    else:
        ng = mid

print(ok)
