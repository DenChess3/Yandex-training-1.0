# n, k = list(map(int, input().split()))
# trees = list(map(int, input().split()))
# kind = {i: 0 for i in range(k)}
# kind[trees[0] - 1] += 1
# right = 0
# ans = (0, n, n + 1)
# for left in range(n - k + 1):
#     while right != n - 1 and any(i == 0 for i in kind.values()):
#         right += 1
#         kind[trees[right] - 1] += 1
#     # print('left, right', left, right)
#     if all(i for i in kind.values()) and ans[2] > right - left + 1:
#         ans = (left + 1, right + 1, right - left + 1)
#     kind[trees[left] - 1] -= 1
#     # print('ans', ans)
#     # print('kind', kind)
# print(ans[0], ans[1])

n, k = list(map(int, input().split()))
trees = list(map(int, input().split()))
kind = {}
kind[trees[0] - 1] = kind.get(trees[0] - 1, 0) + 1
right = 0
ans = (0, n, n + 1)
for left in range(n - k + 1):
    while right != n - 1 and len(kind) != k:
        right += 1
        kind[trees[right] - 1] = kind.get(trees[right] - 1, 0) + 1
    # print('left, right', left, right)
    if len(kind) == k and ans[2] > right - left + 1:
        ans = (left + 1, right + 1, right - left + 1)
    kind[trees[left] - 1] = kind.get(trees[left] - 1, 0) - 1
    if kind[trees[left] - 1] == 0:
        del kind[trees[left] - 1]
    # print('ans', ans)
    # print('kind', kind)
print(ans[0], ans[1])