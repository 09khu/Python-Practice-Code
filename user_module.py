'''import factorial
x=int(input("Enter total : "))
y=int(input("Enter value : "))
fx=factorial.factorial(x)
fy=factorial.factorial(x-y)
p=fx/fy
print("permutation = ",p)
from Factorial_recursion import fact
x=int(input("Enter total : "))
y=int(input("Enter value : "))
fx=fact(x)
fy=fact(x-y)
p=fx/fy
print("permutation = ",p)'''



import Factorial_recursion as f
x=int(input("Enter total : "))
y=int(input("Enter value : "))
fx=f.fact(x)
fy=f.fact(x-y)
p=fx/fy
print("permutation = ",p)