dim=int(input("Enter the dimension"))
elements=input("Enter ther elements")
elements=elements.split(" ")
print(elements)
arr=[x for x in range(dim)]
count=0
def gen(): 
    return elements[count]
for a in range(dim):
    arr[a]=[x for x in range(dim)]
    for b in range(dim):
        arr[a][b]=gen()
        count=count+1
print(arr)
