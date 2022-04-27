from support import *
def smart_div(func):  #decorator
    def inner(m,n):
        if m<n:
            m,n=n,m
            #return m,n
        return func(m,n)
    return inner
       # return(func)
        

a = int(input("Entervalue of a: "))
b = int(input("Entervalue of b: "))
c = div(a,b)
#d = smart_div(a,b)
div1 = smart_div(div)
d = div1(a,b)


print("a = ",a)
print("b = ",b)
print("c = ",c)
print("d = ",d)

# I want division operator if numerator is greator than denomator then it done swapping and ans will not in float


#decorators are function where we can modify the functioning of current available functions
#whenever is called instead of parameters we pass function 



