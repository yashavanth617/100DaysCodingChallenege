def ReverseWordInString(string):
    
    s = string.split()
    w = ""
    l=[]

    for i in s:
        for j in range(len(i)-1,-1,-1):
            w+=i[j]
        l += w + " "
        w=""
        
    print("".join(l))


string = "Hello programmers this is Yashavnth TV GitHub"
ReverseWordInString(string)
