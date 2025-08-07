def SecondBiggestNumber(arr):
    if len(arr) < 2 :
        print("List should conatin atleast 2 elements")
        return
    
    biggest= second_biggest = float('-inf')
    for i in arr:
        if i > biggest:
            second_biggest = biggest
            biggest = i

        if i > second_biggest and i < biggest:
            second_biggest = i
    if second_biggest == float('-inf'):
        print("All the values are equal")
    else:
         print(f"second biggest number is {second_biggest}")


x = [78, 46, 40, 100, 2, 4, 5]
y = [-78, -46, -40, -100, -2, -4, -5]
z=[10,10,10,10]
a=[1]
SecondBiggestNumber(x)
SecondBiggestNumber(y)
SecondBiggestNumber(z)
SecondBiggestNumber(a)
