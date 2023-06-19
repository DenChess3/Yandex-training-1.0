def maxmult(seq):
    def twomaxmult(seq):
        max1 = max(seq[0], seq[1])
        max2 = min(seq[0], seq[1])
        for i in range(2, len(seq)):
            if seq[i] >= max1:
                max2 = max1
                max1 = seq[i]
            elif seq[i] >= max2:
                max2 = seq[i]
        return max1 * max2, max1, max2
    
    def twominmult(seq):
        max1 = min(seq[0], seq[1])
        max2 = max(seq[0], seq[1])
        for i in range(2, len(seq)):
            if seq[i] <= max1:
                max2 = max1
                max1 = seq[i]
            elif seq[i] <= max2:
                max2 = seq[i]
        return max1 * max2, max1, max2

    pos = [i for i in seq if i > 0]
    neg = [i for i in seq if i < 0]
    poszero = [i for i in seq if i >= 0]
    negzero = [i for i in seq if i <= 0]

    amax = [0] * 4

    if len(pos) >= 2:
        amax[0] = twomaxmult(pos)
    else:
        amax[0] = (float('-inf'), 0, 0)

    if len(poszero) >= 2:
        amax[1] = twomaxmult(poszero)
    else:
        amax[1] = (float('-inf'), 0, 0)

    if len(neg) >= 2:
        amax[2] = twominmult(neg)
    else:
        amax[2] = (float('-inf'), 0, 0)

    if len(negzero) >= 2:
        amax[3] = twominmult(negzero)
    else:
        amax[3] = (float('-inf'), 0, 0)

    maxfinalmult = max(amax, key=lambda i: i[0])

    if maxfinalmult[1] < maxfinalmult[2]:
        return str(maxfinalmult[1]) + ' ' + str(maxfinalmult[2])
    else:
        return str(maxfinalmult[2]) + ' ' + str(maxfinalmult[1])
    # a = {pos: True, neg: True, poszero: True, negzero: True}
    # for i in (pos, neg, poszero, negzero):
    #     if len(i) < 2:
    #         a[i] = False

    # can = []
    # for i in (pos, neg, poszero, negzero):
    #     if a[i]:
    #         can.append(i)
    
    # maxfinal = twomaxmult(can[0])[0]
    # for i in can:
    #     if twomaxmult(i)[0] > maxfinal:
    #         maxfinal = twomaxmult(can[i])[0]
    
    # for i in can:
    #     if twomaxmult(i)[0] == maxfinal:
    #         return str(twomaxmult(i)[1]) + ' ' + str(twomaxmult(i)[2])


seq = list(map(int, input().split()))
if len(seq) == 2:
    print(min(seq[0], seq[1]), max(seq[0], seq[1]))
else:
    print(maxmult(seq))
