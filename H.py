def maxmt(seq):
    def maxp3(seq):
        if len(seq) == 1:
            max1 = seq[0]
            max2 = 0
            max3 = 0
        elif len(seq) == 2:
            max1 = max(seq[0], seq[1])
            max2 = min(seq[0], seq[1])
            max3 = 0
        else:
            max1 = max(seq[0], seq[1], seq[2])
            max3 = min(seq[0], seq[1], seq[2])
            max2 = seq[0] + seq[1] + seq[2] - max1 - max3
        for i in range(3, len(seq)):
            if seq[i] >= max1:
                max3 = max2
                max2 = max1
                max1 = seq[i]
            elif seq[i] >= max2:
                max3 = max2
                max2 = seq[i]
            elif seq[i] >= max3:
                max3 = seq[i]
        return max1, max2, max3
    
    def minn2(seq):
        if len(seq) == 1:
            return seq[0], 0
        min1 = min(seq[0], seq[1])
        min2 = max(seq[0], seq[1])
        for i in range(2, len(seq)):
            if seq[i] <= min1:
                min2 = min1
                min1 = seq[i]
            elif seq[i] <= min2:
                min2 = seq[i]
        return min1, min2
    
    pos = [i for i in seq if i >= 0]
    neg = [i for i in seq if i < 0]

    if len(seq) == 3:
        print(' '.join(str(i) for i in sorted(seq, reverse=True)))
    elif all(i < 0 for i in seq):
        max1, max2, max3 = maxp3(seq)
        print(max1, max2, max3, sep=' ')
    elif all(i >= 0 for i in seq):
        max1, max2, max3 = maxp3(seq)
        print(max1, max2, max3, sep=' ')
    else:
        max1, max2, max3 = maxp3(pos)
        min1, min2 = minn2(neg)

        if max2 * max3 >= min1 * min2:
            print(max1, max2, max3, sep=' ')
        else:
            print(max1, min2, min1, sep=' ')


seq = list(map(int, input().split()))
maxmt(seq)