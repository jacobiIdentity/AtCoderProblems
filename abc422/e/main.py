#!/usr/bin/env python3
import sys
import random
from math import gcd

def line_coeff_from_two_points(p, q):
    x1, y1 = p
    x2, y2 = q
    a = y1 - y2
    b = x2 - x1
    c = x1 * y2 - x2 * y1
    # normalize by gcd
    g = gcd(gcd(abs(a), abs(b)), abs(c))
    if g != 0:
        a //= g; b //= g; c //= g
    # sign normalization
    if a < 0 or (a == 0 and b < 0) or (a == 0 and b == 0 and c < 0):
        a, b, c = -a, -b, -c
    return (a, b, c)

def on_same_line(p, q, r):
    # check if p,q,r are collinear using cross product (integer exact)
    (x1, y1), (x2, y2), (x3, y3) = p, q, r
    return (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1)

def find_majority_line_random(points, trials=100, seed=None):
    """
    points: list of (x,y) tuples (distinct points)
    trials: number of random pairs to try
    returns: (True,(a,b,c)) if found, otherwise (False, None)
    """
    n = len(points)
    need = n // 2 + 1
    if n == 0:
        return False, None
    if n == 1:
        x0, y0 = points[0]
        return True, (1, 0, -x0)

    rng = random.Random(seed)
    idxs = list(range(n))
    for t in range(trials):
        i, j = rng.sample(idxs, 2)
        p = points[i]
        q = points[j]
        # quickly count how many points lie on line pq
        cnt = 0
        # we can short-circuit if not reachable, but we'll count fully
        for r in points:
            if on_same_line(p, q, r):
                cnt += 1
                # optional early exit:
                if cnt >= need:
                    coeff = line_coeff_from_two_points(p, q)
                    return True, coeff
    return False, None

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    pts = [tuple(map(int, input().split())) for _ in range(n)]
    # 試行回数は100（ユーザー提案）
    ok, coeff = find_majority_line_random(pts, trials=100, seed=123456)
    if ok:
        print("Yes")
        print(*coeff)
    else:
        print("No")

if __name__ == "__main__":
    main()
