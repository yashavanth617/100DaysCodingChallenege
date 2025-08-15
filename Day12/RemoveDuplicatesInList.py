        
def RemoveDuplicateInList(l):
    i = 0
    for j in range(len(l)):
        duplicate_found = False
        for k in range(i):
            if l[j] == l[k]:
                duplicate_found = True
                break

        if not duplicate_found:
            l[i] = l[j]
            i +=1
    del l[i:]
    print(l)
 

l = ['a','b','a','c','d','b','c','a']
RemoveDuplicateInList(l)
