class pattern:
    def area(self,a=None,b=None):
        if(a!=None and b!=None):
            x = a*b
            return x
        elif(a!=None and b==None):
            x=3.14 *a*a
            return x
        else:
            x = "No values are passed"
            return x

x = pattern()
react=x.area(12,13)
circle=x.area(12)


print("Area of rectangle: ", react)

print("Area of circle: " , circle)
      

