#NOR=1000#Number of run
ipos=[0,0]
fpos=[]
import random
def walk_simu(pos):
    pos[0]+=random.choice([1,-1])
    pos[1]+=random.choice([1,-1])
    return pos
def total_step(step=30):
    realpos=ipos
    for i in range(step):
        realpos=walk_simu(realpos)
    return realpos
def prob_trans(NOR=100,step=30):
    prob_tran=0
    for i in range(NOR):
        realpos=total_step(step)
        if (abs(realpos[0])+abs(realpos[1]))>4:
            prob_tran+=1
    return(prob_tran/NOR)
print(prob_trans(10000,20))
 
#for i in range(20):
#    print(prob_trans(10000,i))
