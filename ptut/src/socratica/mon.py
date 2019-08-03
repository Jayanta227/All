import random
class c1:
    x=0
    y=0
    run=10000
    transport=0
    def rand_walk(self,steps=20):
        c1.x=0
        c1.y=0
        for i in range(steps):
            (dx,dy)=random.choice([(0,1),(0,-1),(1,0),(-1,0)])
            c1.x+=dx
            c1.y+=dy
        return(c1.x,c1.y)
    def chance(self,steps,run):
        c1.transport=0
        for i in range(run):
            pos=c1().rand_walk(steps)
            if abs(pos[1]+pos[0])<5:
                c1.transport+=1
        print('probability of getting transport for'+str(steps)+' steps is :'+ str(c1.transport/run))

for i in range(30):
    c1().chance(i,5000)