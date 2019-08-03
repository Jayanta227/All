fhand=open("hello.txt")
lines=fhand.read()
space=0
line=0
upcase=0
upword=""
print(lines)
for line in lines:
    words=line.split(' ')
    for word in words:
        if word.isupper()==True:
            upword+=word
    for char in line:
        if char==' ':
            space+=1
        if char.isupper()==True:
            upcase+=1
print('space, line, upcase, upword\t'+'\t'+str(space)+',\t'+str(line)+',\t'+str(upcase)+',\t'+upword)