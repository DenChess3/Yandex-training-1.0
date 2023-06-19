n, k, m = map(int, input().split())
cnt = 0
if m > k:
	print(0)
else:
    while n >= k:
        cnt += (n // k) * (k // m)
        n = n % k + (n // k) * (k % m)
    print(cnt)