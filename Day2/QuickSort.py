# Quick Sort

def QucikSort(arr):
     if len(arr) <= 1:
          return arr
     else:
          pivot = arr[0]
          left = [i for i in arr if i < pivot]
          right = [i for i in arr if i > pivot]

          return QucikSort(left) + [pivot] + QucikSort(right)

y = [78,46,40,1,2,4,5]
quick_sort = QucikSort(y)
print(quick_sort)
