xyz = set(map(int, input().split()))
n = set(int(i) for i in input())

print(len(n - (xyz & n)))