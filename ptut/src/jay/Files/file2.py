f=open("txt.txt","r+")
str=""
for line in f:
    lst=line.split(",")
    print(lst[1]+"\b")
    str=str+"sum|: "+lst[0]+","+lst[1]
f.write(str)
print(str)
f.close()
f=open("txt.txt","w")
f.write(str)
f.close()
    