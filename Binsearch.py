# Проверка для поиска ПЕРВОГО подходящего для ОТСОРТИРОВАННОЙ по возрастанию последовательности
# Для ЛЕВОГО lbinsearch
def checkisgreater(index, parametrs):
    seq, x = parametrs
    return seq[index] >= x


# Проверка для поиска ПОСЛЕДНЕГО подходящего для ОТСОРТИРОВАННОЙ по возрастанию последовательности
# Для ЛЕВОГО lbinsearch
def checkisgreaterlast(index, parametrs):
    seq, x = parametrs
    return seq[index] > x


# Проверка для поиска ПОСЛЕДНЕГО подходящего для ОТСОРТИРОВАННОЙ по возрастанию последовательности
# Для ПРАВОГО rbinsearch
def checkisless(index, parametrs):
    seq, x = parametrs
    return seq[index] <= x

# проверка для поиска последнего подходящего


# Ищем первое хорошее вхождение, т.е. 
# до искомого элемнета значения нас не устраивают, после - устраивают
# В параметрах передаем последовательность и искомый элемент
def lbinsearch(left, right, parametrs, check=checkisgreater):
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


# Ищем последнее хорошее значение, т.е.
# до искомого элемнета значения нас устраивают, после - не устраивают
def rbinsearch(left, right, parametrs, check=checkisless):
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


# Ищет первое вхождение в ОТСОРТИРОВАННОМ массиве, если его нет возвращает -1
def findfirst(seq, x):
    ans = lbinsearch(0, len(seq) - 1, (seq, x))
    return -1 if seq[ans] != x else ans


# Ищет последнее вхождение в ОТСОРТИРОВАННОМ массиве, если его нет возвращает -1
def findlast(seq, x):
    ans = rbinsearch(0, len(seq) - 1, (seq, x))
    return -1 if seq[ans] != x else ans


# TEST
# arr = list(map(int, input().split()))
# x = int(input())
# print(findlast(arr, x))
# print(lbinsearch(0, len(arr) - 1, (arr, x)))


# OTHER TEST from task A
# n, k = map(int, input().split())
# arr1 = sorted(list(map(int, input().split())))
# arr2 = list(map(int, input().split()))
# for elem in arr2:
#     if elem <= arr1[-1] and arr1[lbinsearch(0, len(arr1) - 1, (arr1, elem))] == elem:
#         print("YES")
#     else:
#         print("NO")

# SECOND OTHER TEST from task A
# n, k = map(int, input().split())
# arr1 = sorted(list(map(int, input().split())))
# arr2 = list(map(int, input().split()))
# for elem in arr2:
#     index = findlast(arr1, elem)
#     print("NO" if index == -1 else "YES")
