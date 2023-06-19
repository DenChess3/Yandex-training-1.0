n = int(input())
lst = list(map(int, input().split()))
x = int(input())

min_dist = abs(lst[0] - x)
elem = lst[0]
for i in range(n):
    if abs(lst[i] - x) < min_dist:
        elem = lst[i]
        min_dist = abs(lst[i] - x)
print(elem)