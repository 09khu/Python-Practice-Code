import recursion

x=int(input("Enter value of n: "))
y=int(input("Enter value of r : "))
fx=recursion.fact(x)
fy=recursion.fact(x-y)
p=fx/fy
print("p = ",p)  


