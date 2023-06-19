def rbinsearch(left, right, parametrs, check):
    while left < right:
        # берем середину отрезка и добавляем единицу для сходимости
        mid = (left + right + 1) // 2
        if check(mid, parametrs):
            left = mid
        else:
            # опять же единица для сходимости, там добавили тут вычли
            right = mid - 1
    # указатели сошлись, возвращаем один из них
    return left


def checkmodule(d, parametrs):
    n, a, b, w, h = parametrs
    return (max(w, h) // (min(a, b) + 2 * d)) * (min(w, h) // (max(a, b) + 2 * d)) >= n


n, a, b, w, h = map(int, input().split())
print(rbinsearch(0, max(w, h) // n, (n, a, b, w, h), checkmodule))