#!/usr/bin/env python3
n = input()
print(n[:3]+'0'*(len(n)-3))
# n = int(input())
# if n < 10**3 :
#     print(n)
# elif n < 10**4 :
#     print(n-n%(10**1))
# elif n < 10**5 :
#     print(n-n%(10**2))
# elif n < 10**6 :
#     print(n-n%(10**3))
# elif n < 10**7 :
#     print(n-n%(10**4))
# elif n < 10**8 :
#     print(n-n%(10**5))
# else :
#     print(n-n%(10**6))