import re
print("do you want to write a line or want to link a file")
ans=input("type 1 for writting and 2 for linking: ")
if ans=="1":
    strn=input("type your line :\n")
    regx=input("type your expression :")
    matches=re.findall(regx,strn)
    print(matches)
else:
    fname=input("Enter a file name")
    regx=input("Enter an expression")
    fhand=open(fname)
    for line in fhand:
        line=line.rstrip()
        matches=re.findall(regx,line)
        if len(matches)>0:
            print(matches)
            print("line: ",line)
