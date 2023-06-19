from Binsearch import rbinsearch


n, k = map(int, input().split())
arr1 = sorted(list(map(int, input().split())))
arr2 = list(map(int, input().split()))
for elem in arr2:
    index = rbinsearch(0, len(arr1) - 1, (arr1, elem))
    print(arr1[index] if index == n - 1 or elem - arr1[index] <= arr1[index + 1] - elem else arr1[index + 1])