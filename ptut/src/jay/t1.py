#calculation for searching a given number from a list
str=input("enter your words seperated by spacing")
arr=str.split()
print(arr)
j=0
noword=[]
print("length of the arr is")
print(len(arr))
for x in arr:
    i=0
    noword.append(0)
    while i<len(arr):
        if x==arr[i]:
            noword[j]=noword[j]+1
        i=i+1
    j=j+1

print(noword)
