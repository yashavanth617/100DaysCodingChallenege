def MergeTwoSortedArray(arr1, arr2):
    i = j = 0
    merge = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merge.append(arr1[i])
            i += 1
        else:
            merge.append(arr2[j])
            j += 1
        
    while i < len(arr1):
        merge.append(arr1[i])
        i += 1

    while j < len(arr2):
        merge.append(arr2[j])
        j += 1
    
    print(merge)

arr1 = [1,2,8,9,9,22,35,37,38]
arr2 = [2,3,4,5,6,7,20,21,33,36,39,40,45,88]

MergeTwoSortedArray(arr1, arr2)
