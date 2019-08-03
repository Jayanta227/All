f=open("txt.txt","r")
def count(n):
    flag=0
    for line in f:
        if n in line:
            flag=flag+1
    return flag
repeatation=count("9")
print(repeatation)
