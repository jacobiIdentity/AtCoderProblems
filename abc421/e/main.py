from decimal import Decimal, getcontext
from functools import lru_cache
from itertools import product
from math import comb

# 精度を十分に高く設定
getcontext().prec = 50

def multinomial_prob(hist, p_each):
    n = sum(hist)
    coeff = Decimal(1)
    rem = n
    for h in hist[:-1]:
        coeff *= Decimal(comb(rem, h))
        rem -= h
    return coeff * (Decimal(p_each) ** n)

def multinomial_histograms(n, k=6):
    def gen(pos, remaining, curr):
        if pos == k - 1:
            yield tuple(curr + [remaining])
            return
        for x in range(remaining + 1):
            yield from gen(pos + 1, remaining - x, curr + [x])
    return list(gen(0, n, []))

def expected_best_score(A):
    A = tuple(A)
    p = Decimal('1')/Decimal('6')
    HISTS = {n: multinomial_histograms(n, 6) for n in range(6)}
    PROB  = {n: {h: multinomial_prob(h, p) for h in HISTS[n]} for n in range(6)}

    values = sorted(set(A))
    idxs = {v: [i for i,a in enumerate(A) if a == v] for v in values}

    @lru_cache(None)
    def V(r, c):  # c: 長さ6タプル
        if r == 0:
            best = Decimal(0)
            for v in values:
                s = sum(c[i] for i in idxs[v])
                val = Decimal(s) * Decimal(v)
                if val > best:
                    best = val
            return best

        best = Decimal('-1')
        for s in product(*(range(x + 1) for x in c)):
            kept = sum(s)
            if kept > 5:
                continue
            m = 5 - kept
            val = Decimal(0)
            for h, ph in PROB[m].items():
                nxt = tuple(s[j] + h[j] for j in range(6))
                val += ph * V(r - 1, nxt)
            if val > best:
                best = val
        return best

    ans = Decimal(0)
    for c, pc in PROB[5].items():
        ans += pc * V(2, c)
    return ans

if __name__ == "__main__":
    import sys
    A = list(map(int, sys.stdin.read().strip().split()))
    result = expected_best_score(A)
    # 小数点以下10桁まで出力
    print(f"{result:.10f}")
