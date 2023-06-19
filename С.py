# from Binsearch import lbinsearch


# def checkboard(size, parametrs):
#     w, h, n = parametrs
#     return (size // w) * (size // h) >= n


# w, h, n = map(int, input().split())
# print(lbinsearch(0, n * min(w, h), (w, h, n), checkboard))

def lbinsearch(left, right, parametrs, check):
    while left < right:
        # берем середину отрезка
        mid = (left + right) // 2
        # check - функция, проверяющая, устраивает нас значение или нет
        if check(mid, parametrs): 
            right = mid
        else:
            left = mid + 1
            # плюс один надо для того, чтобы указатели сошлись на одном элементе
    # left = right, т.е. указатели сошлись на одном элементе
    return left


def checkboard(size, parametrs):
    w, h, n = parametrs
    return (size // w) * (size // h) >= n


w, h, n = map(int, input().split())
print(lbinsearch(0, n * min(w, h), (w, h, n), checkboard))