#Bubble Sort
def BubbleSort(arr):
    for i in range(len(arr)):
        swaped = False
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
                swaped =True
        
        if not swaped:
            break
    return arr
x = [78,46,40,100,2,4,5]
print(BubbleSort(x))
