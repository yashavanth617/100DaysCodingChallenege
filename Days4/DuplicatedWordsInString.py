# Print Dupicate Values In String

def DuplicatedValuesINString(string):
    l=[]
    s= set()
    for i in string:
        if i != " ":
            if i not in l:
                l+= i
            else:
                s.add(i)
    print(s)

string = "Duplicated values are Founded here"
DuplicatedValuesINString(string)
