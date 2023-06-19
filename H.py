n, k = map(int, input().split())
s = input()
right = 0
ans = (1, 0) # first is start, second is length
d = {}
len_top = 0
for left in range(n):
    while right != n and all(i <= k for i in d.values()):
        d[s[right]] = d.get(s[right], 0) + 1
        right += 1
        len_top += 1
    if ans[1] < len_top - 1:
        ans = (left + 1, len_top - 1)
    len_top -= 1
    d[s[left]] = d.get(s[left], 0) - 1
print(ans[1], ans[0])