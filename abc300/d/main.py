n = int(input())
root = int(pow(n,0.5))
nums = [i for i in range(root+1)]
for i in range(2,root + 1):
    if nums[i] != 0:
        for j in range(i, root+1):
            if i*j >= root+1:
                break
            nums[i*j] = 0
primes = sorted(list(set(nums)))[2:]
ans = 0
for i in primes :
    if i**5 > n : break
    for j in primes :
        if j <= i : continue
        if (i**2) * (j**3) > n : break
        for k in primes :
            # print((i**2) * j * (k**2))
            if k <= j or k <= i : continue
            if (i**2) * j * (k**2) > n : break
            ans += 1
# print(primes)
print(ans)