class vehicle:
    def __init__(self):
        print("transportation")
        have_wheels=True
class bike(vehicle):
    def special_use(self):
        print("road trip")
    def __init__(self):
        self.wheels=2
class car(vehicle):
    def special_use(self):
        print("family tour")
    #def __init__(self):
        #self.wheels=4

c=car()
c.special_use()