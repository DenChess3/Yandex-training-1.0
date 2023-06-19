def binsearch(x, arr):
    # print('ELEMENT', x)
    left, right = 0, len(arr) - 1
    while left < right:
        # print("left, right", left, right)
        m = (right + left) // 2
        if x <= arr[m]:
            right = m
        else:
            left = m + 1
    # print('end', left, right)
    return left
    

n, k = map(int, input().split())
arr1 = sorted(list(map(int, input().split())))
arr2 = list(map(int, input().split()))
for elem in arr2:
    if elem <= arr1[-1] and arr1[binsearch(elem, arr1)] == elem:
        print("YES")
    else:
        print("NO")