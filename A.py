n = int(input())
shirts = list(map(int, input().split()))
m = int(input())
shorts = list(map(int, input().split()))

second = 0
top_shirts = 0
top_shorts = 0
top_diff = abs(shirts[0] - shorts[0])
for first in range(n):
    while shirts[first] > shorts[second] and second != m - 1:
        second += 1 
    if top_diff > abs(shirts[first] - shorts[second]):
        top_diff = abs(shirts[first] - shorts[second])
        top_shirts = first
        top_shorts = second
    if second != 0 and top_diff > abs(shirts[first] - shorts[second - 1]):
        top_diff = abs(shirts[first] - shorts[second - 1])
        top_shirts = first
        top_shorts = second - 1
print(shirts[top_shirts], shorts[top_shorts])