import random
def random_walk(n):
    x,y=0,0
    for i in range(n):
        (dx,dy)=random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        y+=dx
        x+=dy
    return (x,y)

cycle=20000
steps=30
transport_count=0
for stp in range(steps):
    transport_count=0
    for i in range(cycle):
        (x,y)=random_walk(stp)
        if abs(x)+abs(y)>4:
            transport_count+=1
    prob_trans=transport_count/cycle
    print("step ",stp,"probability of transport required :",prob_trans)
