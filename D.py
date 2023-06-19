n, r = list(map(int, input().split()))
d = list(map(int, input().split()))
# dist = [d[i + 1] - d[i] for i in range(n - 1)]
right = 1
var = 0

for left in range(n - 1):
    dist = d[right] - d[left]
    # print("dist ", dist)
    while right != n - 1 and dist <= r:
        right += 1
        dist = d[right] - d[left]
    # print('l r', left, right)
    if dist > r:
        var += n - right
    # print('var', var)
print(var)

# for left in range(n - 1):
#     if right != n - 1:
#         dist = d[right] - d[left]
#         while right < n and dist <= r:
#             right += 1
#             dist = d[right] - d[left]
#         var += n - right
#     else:
#         if d[right] - d[left] > r:
#             var += 1
#         else:
#             break
# print(var)