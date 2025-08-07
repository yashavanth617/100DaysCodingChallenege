# Reversing a word in String
def ReverseWordInString(string):
    
    s = string.split()
    w = ""
    l=[]

    for i in s:
        for j in range(len(i)-1,-1,-1):
            w+=i[j]
        l.append(w)
        w=""
    
    print(s)
    print(" ".join(l))


string = "Hello Programmers Welcome To My GitHub This Is Yashavanth TV"
ReverseWordInString(string)
