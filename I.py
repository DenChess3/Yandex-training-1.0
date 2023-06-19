n = int(input())
setall = set()
setonly = set()
for i in range(n):
    m = int(input())
    setone = set()
    for j in range(m):
        elem = input()
        setall.add(elem)
        setone.add(elem)
    if i == 0:
        setonly = set(setall)
    setonly = setonly & setone
print(len(setonly))
for leng in setonly:
    print(leng)
print(len(setall))
for leng in setall:
    print(leng)