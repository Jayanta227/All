import sqlite3
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.app import App
from kivy.uix.textinput import TextInput
import matplotlib.pyplot as plt
from kivy.uix.image import Image
from kivy.uix.button import Button
bis=None


class Screen1(Screen):
    def plotting(self):
        
        global bis
        q=abs(bis.llim-bis.ulim)/100
        x=[bis.llim+i*q for i in range(99)]
        y=[bis.fun_cal(i) for i in x]
        plt.clf()
        plt.plot(x,y)
        plt.plot([bis.llim,bis.ulim],[0,0])
        
        plt.savefig('graph.png')
        #plt.show()
        im=Image(source='graph.png',allow_stretch=True,keep_ratio=False)
        im.reload()
        self.ids.grph.add_widget(im)
        
    def input_taking(self):
        global bis
        arr=self.ids.t1.text.split(',')
        bis.fun=[float(i) for i in arr]
        bis.order=len(arr)-1
        #self.fun=[3,-2,-10]
        lim=self.ids.rn.text.split(',')
        bis.llim=float(lim[0])
        bis.ulim=float(lim[1])
    
    
    
    
    
class Screen2(Screen):
    def pop_tab(self):
        conn=sqlite3.connect('bis.db')
        c=conn.cursor()
        c.execute("select * from mytable")
        f=c.fetchall()
        #print(f)
        for row in f:
            for cols in row:
                t=TextInput(text=str(cols))
                self.ids.gd.add_widget(t)
        
        conn.commit()
        c.close()
        conn.close()
class Screen3(Screen):
    pass
    

class Bis(ScreenManager):
    llim=1
    ulim=3
    order=2
    fun=[3,-2,-10]
    conn=0
    c=0
    

    def fun_cal(self,x):
        order=self.order
        y=0
        for _ in self.fun:
            y=y+_*(x**order)
            order-=1
        return y
    def ini_range(self):
        pass
    def tab_hed(self):
        self.conn=sqlite3.connect('bis.db')
        self.c=self.conn.cursor()
        self.c.execute("drop table if exists mytable")

        self.c.execute("create table if not exists mytable (llim REAL, ulim REAL, mpoint REAL, fun REAL)")
    def root_cal(self):
        llim=self.llim
        ulim=self.ulim
        mpoint=(ulim+llim)/2
        fun=self.fun_cal(mpoint)
        new_mpoint=0
        if fun==0:
        
            self.c.execute("insert into mytable (llim,ulim,mpoint,fun) values (?,?,?,?)",(llim,ulim,mpoint,fun))

            
        elif self.fun_cal(llim)*self.fun_cal(ulim)<0:
            for _ in range(30):
                mpoint=(ulim+llim)/2
                if self.fun_cal(mpoint)*self.fun_cal(llim)<0:
                    ulim=mpoint
                    new_mpoint=(ulim+llim)/2
                    fun=self.fun_cal(new_mpoint)
                    
                    
                elif self.fun_cal(new_mpoint)==0:
                    self.conn.commit()
                    self.c.close()
                    self.conn.close()
                    return 0
                elif self.fun_cal(mpoint)*self.fun_cal(ulim)<0:
                    llim=mpoint
                    new_mpoint=(ulim+llim)/2
                    
                    fun=self.fun_cal(new_mpoint)
                print("I am executing")
                self.c.execute("insert into mytable (llim,ulim,mpoint,fun) values (?,?,?,?)",(llim,ulim,new_mpoint,fun))
        self.conn.commit()
        self.c.close()
        self.conn.close()
    
   
        
class RootApp(App):
    def build(self):
        global bis
        bis= Bis()
        return bis
if __name__=='__main__':
    RootApp().run()
    # bis.input_taking()
    # bis.tab_hed()
    # bis.root_cal()
    # print(bis.fun_cal(3)*bis.fun_cal(1))
     