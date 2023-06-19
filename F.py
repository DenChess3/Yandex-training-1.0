n, power, m, cond, second, total = int(input()), sorted(list(map(int, input().split()))), int(input()), [], 0, 0
for i in range(m):
    cond.append(tuple(map(int, input().split())))
cond.sort(key=lambda x: x[1])
for first in range(n):
    while cond[second][0] < power[first]:
        second += 1
    total += cond[second][1]
print(total)