def InsertNewElemnet(x, elemnet, pos):
    if pos > len(x):
        print("Out Of Index")
        return
    l = [0] * (len(x)+1)
    c=0
    for i in range(pos-1):
        l[c] = x[i]
        c+=1

    l[c] = elemnet

    for i in range(pos-1, len(x)):
        c+=1
        l[c] = x[i]

    print(l)

x = [1,2,3,4,5,6]
Insert =InsertNewElemnet(x, 100, 4)
