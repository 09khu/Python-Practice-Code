import recursion

x=int(input("Enter value of n: "))
y=int(input("Enter value of r : "))
z=recursion.fact(y)
fx=recursion.fact(x)
fy=recursion.fact(x-y)
c=fx/(z*fy)
print("combination= ",c) 