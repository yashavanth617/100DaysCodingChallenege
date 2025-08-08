def DeleteElementByIndexInList(x, index):
    if index > len(x):
        print("out of index range")
        return
    
    c= 0
    l = [0] * (len(x)-1)
    for i in range(index-1):
        l[c] = x[i]
        c+=1

    for i in range(index, len(x)):
        l[c] = x[i]
        c+=1

    print(l)
x = [1,2,3,4,5,6]
DeleteElementByIndexInList(x,4)
