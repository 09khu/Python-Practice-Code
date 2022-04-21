#Program to calculate 

def fact(n):
    fact_n=1
    for i in range(1,n+1):
        fact_n*=i
        return(fact_n)
        
x=int(input("Enter total : "))
y=int(input("Enter value : "))
fx=fact(x)
fy=fact(x-y)
p=fx/fy
print("p = ",p)  


#Program to calculate Area and circumference of the circle

'''pi = 3.14
def Circle(r):
	return (pi*r*r, 2*pi*r)
radius = float(input("Enter the Radius: "))
(area, circum) = Circle(radius)
print ("Area of the circle = ", area)
print ("Circumference of the circle = ", circum)'''
