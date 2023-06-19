from Binsearch import lbinsearch


def checkboard(size, parametrs):
    w, h, n = parametrs
    return (size // w) * (size // h) >= n


w, h, n = map(int, input().split())
print(lbinsearch(0, n * min(w, h), (w, h, n), checkboard))