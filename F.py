na, nb, ma, mb = map(int, input().split())
v1 = (na + ma) * max(nb, mb)
v2 = (na + mb) * max(nb, ma)
v3 = (nb + mb) * max(na, ma)
v4 = (nb + ma) * max(na, mb)
vmin = min(v1, v2, v3, v4)
if vmin == v1:
    print(na + ma, max(nb, mb))
elif vmin == v2:
    print(na + mb, max(nb, ma))
elif vmin == v3:
    print(nb + mb, max(na, ma))
elif vmin == v4:
    print(nb + ma, max(na, mb))
