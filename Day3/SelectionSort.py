# Selection Sort
def SelectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

x = [78, 46, 40, 100, 2, 4, 5]
print(SelectionSort(x))
