n = int(input())
max_click = [0] + list(map(int, input().split()))
k = int(input())
clicks = list(map(int, input().split()))
clicks_button = [0] * (n + 1)
for i in clicks:
    clicks_button[i] += 1
for i in range(1, n + 1):
    if max_click[i] >= clicks_button[i]:
        print("NO")
    else:
        print("YES")
