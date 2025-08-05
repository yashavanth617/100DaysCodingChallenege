# Linear Search

def LinearSearch(n,target):
    for i in range(len(n)):
        if n[i] == target:
            print(f"{target} is found at {i}")
            break
    else:
        print(f"{target} is not found")

x=[1,2,3,4,5,6,7,8,9,10]
y = [1,8,7,5,40,3,2,49,51,57,21,4]

LinearSearch(x,51)
