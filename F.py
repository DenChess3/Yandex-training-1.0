def to_symmetrical(n, seq):
    def issym(seq):
        return seq == seq[::-1]
    
    if issym(seq):
        return (0, [])
    for i in range(n - 1, -1, -1):
        if issym(seq + seq[i::-1]):
            ans = (len(seq[i::-1]), seq[i::-1])
    return ans
            

n = int(input())
seq = list(map(int, input().split()))
ans = to_symmetrical(n, seq)
print(ans[0])
print(' '.join(str(i) for i in ans[1]))