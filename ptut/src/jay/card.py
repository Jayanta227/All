arr=[1,2,3,4,5,6,7,8,9,10]
arr.reverse()
arr2=[]

def decode(n):
    for i in n:
        if n.index(i)==len(n)-1:
            arr2.insert(0, i)
            break
        else:
            arrange(i)


def arrange(i):
    arr2.insert(0,i)
    arr2.insert(0,arr2[len(arr2)-1])
    arr2.__delitem__(len(arr2)-1)

decode(arr)
print(arr2)