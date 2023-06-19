def uniqnumbers(seq):
    a = set()
    k = 0
    for i in range(len(seq)):
        if seq[i] not in a:
            a.add(seq[i])
            k += 1
    return k


seq = list(map(int, input().split()))
print(uniqnumbers(seq))

print(' '.join(str(i) for i in sorted(list(set(map(int, input().split())) & set(map(int, input().split()))))))