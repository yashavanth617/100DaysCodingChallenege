def TwoSum(n,target):
    d = {}
    l = []
    for i in range(len(n)):
        d[n[i]] = i
        rem = target - n[i]

        if rem in d:
            l.append(d[rem])
            l.append(i)
    return l
