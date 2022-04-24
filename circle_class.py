
   
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
c1=circle(15)
print(c1.area())