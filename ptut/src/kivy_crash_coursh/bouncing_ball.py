from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


Builder.load_string('''
#:import main main
<Root>:
	rp:round_pos
	orientation:'vertical'
	BoxLayout:
		orientation:'horizontal'
		size_hint_y:None
		height:50
		canvas:
			Color:
				rgba:1,0,0,1
			Rectangle:
				pos:self.pos
				size:self.size
		Button:
			text:"Start Animation"
			on_press:main.round.update()
				
		Button:
			text:"Stop Animation"	
	BoxLayout:
		canvas:
			Color:
				rgba:.3,.6,.6,.7
			Rectangle:
				size:self.size
				pos:self.pos
		Round:
			id:round_pos
<Round>:
	size_hint:None,None
	size:100,100
	pos:50,50
	canvas:
		Color:
			rgba:1,.5,0,.8
		Ellipse:
			size:self.size
			pos:root.velocity
				
''')
class Root(BoxLayout):
	velocity=[15,20]
# 	def __init__(self, **kwargs):
# 		super(Root, self).__init__(**kwargs)
# 	def update(self,*args):
# 		
# 		#Clock.schedule_interval(self.update,1/60)
# 		Round().x=200
# 		Round().y=200
# 	def update(self,*args):
# 		print(Round().ids['el'])
# 		self.velocity[1]+=1
# 		if self.velocity[0] < 0 or (self.velocity + self.width) > Window.width:
# 			self.velocity[0] *= -1
# 		if self.velocity[1] < 0 or (self.velocity + self.width) > Window.width:
# 			self.velocity[1] *= -1
	
class Round(Widget):
	def __init__(self, **kwargs):
		super(Round, self).__init__(**kwargs)
	def update(self,*args):
		
		#Clock.schedule_interval(self.update,1/60)
		Round().x=200
		Round().y=200
runTouchApp(Root())