import random
dq=dict()
bias=[]
da=dict()
number_q=100
def q_making(a=1,b=3,c=1,d=0,n=number_q):
    
    for x in range(a):
        bias.append('a')
    for x in range(b):
        bias.append('b')
    for x in range(c):
        bias.append('c')
    for x in range(d):
        bias.append('d')
        
    for i in range(1,n+1):
        dq[i]=random.choice(bias)
    return dq
def a_making1():
    '''it provides random answering'''
    for x in range(1,1+number_q):
        da[x]=random.choice(['a','b','c','d'])
    return da
def a_making2():
    '''it provides sequential answering'''
    for x in range(1,number_q+1):
        if x%4==1:
            da[x]='a'
        elif x%4==2:
            da[x]='b'
        elif x%4==3:
            da[x]='c'
        else:
            da[x]='d'
    return da
def a_making3(block=4):
    '''it provides block answering'''
    n=0
    b=1
    options=['a','b','c','d']
    for x in range(1,number_q+1):
        if n==block:
            n=0
            b+=1
        if x<=b*block:
            da[x]=options[b%block-1]
            n+=1
    return da
