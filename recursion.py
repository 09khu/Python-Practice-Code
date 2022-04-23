#Program to calculate  factorial through recursion

def fact(x):
    y=1
    if x==1 or x==0:
       return y
    else:
        y=x*fact(x-1)
        return y
'''val=int(input("Enter a value:"))
funct_val=fact(val)
print("Factorial of {} is {}".format(val,funct_val))'''

