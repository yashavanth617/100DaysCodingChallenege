def LeftRoationOfList(x,n):
    n = n % len(x)
    l = [0] * len(x)
    c=0
    for i in range(n, len(x)):
        l[c] = x[i]
        c+=1
    
    for i in range(n):
        l[c] = x[i]
        c+=1
    
    print(l)
x = [1,2,3,4,5,6]
LeftRoationOfList(x, 2)
LeftRoationOfList(x, 12)
