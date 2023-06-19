a, b, c = int(input()), int(input()), int(input())
if c < 0 or a == 0 and b != c ** 2 or a != 0 and round((c ** 2 - b) / a) != (c ** 2 - b) / a:
    print("NO SOLUTIONS")
elif a == 0 and b == c ** 2:
    print("MANY SOLUTIONS")
else:
    print((c ** 2 - b) / a)