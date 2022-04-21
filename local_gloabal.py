'''def user_input():
	a=int(input("enter value 1: "))
	b=int(input("enter value 2: "))
	return(a,b)

def add(a,b):
	return a+b

a,b=user_input()
add(a,b)
print(a,"+",b,"=",add(a,b))	'''


# a,b=int(input("Enter first number\n")),int(input("Enter second number\n"));


#local and global 


count = 1
def plus():
	global count
	count+=1

def minus():
	global count
	count-=1
print("count=",count)

plus()
plus()
minus()
minus()

print("count=",count)

   