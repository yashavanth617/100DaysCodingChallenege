
def TwoPointer(arr):
    left = 0
    right = len(arr)-1
    max_count = 0

    while left < right:
        base = right-left
        height = min(arr[left], arr[right])
        current = base * height
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
        max_count = max(current, max_count)

    print(max_count)

arr = [3,1,1,2,1,2,2,1]
TwoPointer(arr)
