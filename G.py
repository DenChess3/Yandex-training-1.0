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


def checktile(k, param):
    n, m, t = param
    return 2 * k * (n - k + m - k) <= t


n = int(input())
m = int(input())
t = int(input())
print(rbinsearch(0, min(n, m) // 2 + 1, (n, m, t), checktile))