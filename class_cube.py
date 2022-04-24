
class cube:
    def __init__(self):
        self.side=int(input('Enter the length of the side of cube : '))
    def ws_area(self):
        return 6*self.side*self.side
    def ls_area(self):
        return 4*self.side*self.side
    def volume(self):
        return self.side*self.side*self.side
c1=cube()
print("Whole Surface Area  =",c1.ws_area(),"sq. units")
print("Lateral Surface Area  =",c1.ls_area(),"sq. units")
print("Volume  =",c1.volume(),"cu. units")