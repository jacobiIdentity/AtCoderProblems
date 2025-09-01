#!/usr/bin/env python3
from decimal import Decimal,ROUND_HALF_UP
a,b = map(int,input().split())
print(Decimal(b/a).quantize(Decimal('0.001'),ROUND_HALF_UP))