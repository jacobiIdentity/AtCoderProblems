#!/usr/bin/env python3
import math
r, d = map(int, input().split())
print('{:.16f}'.format(2 * math.pi * d * math.pi * r * r))
