class Employee:
    increment=1.5
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lanme=lname
        self.salary=salary
    def increase(self):
        self.salary=int(self.salary)*int(self.increment)
    @classmethod
    def change_increment(cls,amount):
        cls.increment=amount
    @classmethod
    def from_str(cls,splt_str):
        fname,lname,salary=splt_str.split('-')
        return cls(fname,lname,salary)
    
lovish=Employee.from_str('lovish-jackson-30000')
harry=Employee("harry",'potter',20000)
rohon=Employee('rohon','das',20000)
print(rohon.salary)
Employee.change_increment(2)
harry.increase()
print(harry.salary)
print(lovish.__dict__)
print(harry.__dict__)

