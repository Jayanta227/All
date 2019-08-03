from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

class Swimmer():
    velocity=0
    position=0
class RootWid(BoxLayout):
    time_interval=1/55.0
    time=0
    swimmer1=Swimmer()
    swimmer2=Swimmer()
    def do_start(self,t1,t2):

        self.swimmer1.velocity=t1
        self.swimmer2.velocity=t2
        Clock.schedule_interval(self.update, self.time_interval)
        pass
    def update(self,dt):
    
        vel1,pos1=self.vel_pos(self.swimmer1)
        vel2,pos2=self.vel_pos(self.swimmer2)
        
        self.ids.swimmer1.pos[0]=pos1
        self.ids.swimmer2.pos[0]=pos2
        print(dt)
        
        if vel1*vel2<0 and abs(self.swimmer1.position-self.swimmer2.position)<self.time_interval*(abs(vel1)+abs(vel2))/2:
            s='Time: '+str(round(self.time,2))+' ; position: '+str(round(self.swimmer1.position,2))
            #print(s)
            self.ids.labl.text+='  '+s+'\n'
        
        self.time+=self.time_interval
        pass
        
    def vel_pos(self,swimmer):
        lent=10
        vel=abs(swimmer.velocity)
        if (self.time//(lent/vel))%2==0:
            swimmer.velocity=vel
            swimmer.position=(self.time*vel)%lent
        else:
            swimmer.velocity=0-vel
            swimmer.position=lent-(self.time*vel)%lent
        
        pos=swimmer.position*(self.ids.box.size[0]-10)/lent
        return (swimmer.velocity,pos)
        pass
    
    
class SwimApp(App):
    def build(self):
        return RootWid()
if __name__=='__main__':
    SwimApp().run()