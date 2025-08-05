# Binary Search

def BiarySearch(n, target):
    low = 0
    high =len(n)-1
    

    while low <= high:
        mid = (low + high) // 2
        if n[mid] == target:
            print(f"{target} is fount at {mid} position")
            return
        elif n[mid] < target:
            low = mid + 1
        else:
            high = mid-1
    else:
        print("Target is not Found")

x=[1,2,3,4,5,6,7,8,9,10]
y = [1,8,7,5,40,3,2,49,51,57,21,4]
y= sorted(y)

BiarySearch(x,8) 
