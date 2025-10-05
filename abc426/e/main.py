#!/usr/bin/env python3
import sys, math

def min_on_interval(r0x, r0y, vx, vy, L):
    # 距離最小値（ユークリッド） on s∈[0,L] for r(s)=r0 + v*s
    if L <= 0:
        return math.hypot(r0x, r0y)
    vv = vx*vx + vy*vy
    if vv == 0.0:
        return math.hypot(r0x, r0y)
    dot = r0x*vx + r0y*vy
    s = -dot / vv
    if s < 0.0:
        s = 0.0
    elif s > L:
        s = L
    x = r0x + vx*s
    y = r0y + vy*s
    return math.hypot(x, y)

def solve_case(TSX, TSY, TGX, TGY, ASX, ASY, AGX, AGY):
    # ベクトル・長さ
    tx = TGX - TSX
    ty = TGY - TSY
    ax = AGX - ASX
    ay = AGY - ASY
    Tlen = (tx**2+ty**2)**(1/2)
    Alen = (ax**2+ay**2)**(1/2)

    # 単位速度ベクトル（移動しないなら(0,0)）
    if Tlen > 0:
        vT_x = tx / Tlen; vT_y = ty / Tlen
    else:
        vT_x = vT_y = 0.0
    if Alen > 0:
        vA_x = ax / Alen; vA_y = ay / Alen
    else:
        vA_x = vA_y = 0.0

    ans = float('inf')

    # 区間1：両者移動 [0, L1]
    L1 = min(Tlen, Alen)
    r0x = TSX - ASX; r0y = TSY - ASY
    vrx = vT_x - vA_x; vry = vT_y - vA_y
    ans = min(ans, min_on_interval(r0x, r0y, vrx, vry, L1))

    # 区間2：どちらかだけ移動 [L1, L2]
    if Tlen < Alen:
        # Tは到着済みで停止、Aのみが動く
        # 区間開始時の相対位置：TG - (AS + vA*L1)
        a_x = ASX + vA_x*L1; a_y = ASY + vA_y*L1
        r0x = TGX - a_x; r0y = TGY - a_y
        vrx = -vA_x; vry = -vA_y
        ans = min(ans, min_on_interval(r0x, r0y, vrx, vry, Alen - L1))
    elif Alen < Tlen:
        # Aは到着済みで停止、Tのみが動く
        t_x = TSX + vT_x*L1; t_y = TSY + vT_y*L1  # ここでは L1=Alen
        r0x = t_x - AGX; r0y = t_y - AGY
        vrx = vT_x; vry = vT_y
        ans = min(ans, min_on_interval(r0x, r0y, vrx, vry, Tlen - L1))

    # 区間3：両者停止（一定距離）
    ans = min(ans, math.hypot(TGX - AGX, TGY - AGY))

    return ans

def main():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        TSX = float(next(it)); TSY = float(next(it))
        TGX = float(next(it)); TGY = float(next(it))
        ASX = float(next(it)); ASY = float(next(it))
        AGX = float(next(it)); AGY = float(next(it))
        res = solve_case(TSX, TSY, TGX, TGY, ASX, ASY, AGX, AGY)
        # 誤差要件に合わせて桁数は調整（下は十分多め）
        out.append(f"{res:.10f}")
    print("\n".join(out))

if __name__ == "__main__":
    main()
