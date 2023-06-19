n, k = list(map(int, input().split()))
cars = list(map(int, input().split()))
cnt = 0
left = 0
right = 0
sumnow = 0
for left in range(n):
    while right < n and sumnow + cars[right] <= k:
        sumnow += cars[right]
        right += 1
    if sumnow == k:
        cnt += 1
    sumnow -= cars[left]
print(cnt)