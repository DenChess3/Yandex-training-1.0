nm = list(map(int, input().split()))
n, m = nm[0], nm[1]
a = set()
b = set()
for i in range(n):
	a.add(int(input()))
for i in range(m):
	b.add(int(input()))

print(len(a & b))
print(" ".join(str(i) for i in sorted(list(a & b))))

print(len(a - (a & b)))
print(" ".join(str(i) for i in sorted(list(a - (a & b)))))

print(len(b - (a & b)))
print(" ".join(str(i) for i in sorted(list(b - (a & b)))))
