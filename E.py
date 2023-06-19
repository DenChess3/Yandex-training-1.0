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


def checkscore(d, param):
    a, b, c = param
    return 2 * a + 3 * b + 4 * c + 5 * d >= (a + b + c + d) * 3.5


a = int(input())
b = int(input())
c = int(input())
print(lbinsearch(0, a + b + c, (a, b, c), checkscore))