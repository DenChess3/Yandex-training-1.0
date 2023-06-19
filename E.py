n = int(input())
blocks = dict()
for i in range(n):
    w, h = list(map(int, input().split()))
    blocks[w] = max(blocks.get(w, 0), h)
print(sum(blocks.values()))