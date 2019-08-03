import random
def random_walk(n):
    x=0
    y=0
    for i in range(n):
        step=random.choice(['n','s','e','w'])
        if step=='n':
            y=y+1
        elif step=='s':
            y=y-1
        elif step=='e':
            x=x+1
        elif step=='w':
            x=x-1
    return (x,y)
for i in range(25):
    walk=random_walk(10)
    print(walk,"distance from home= ",abs(walk[0]+abs(walk[1])))
