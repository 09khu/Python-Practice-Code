#Welcome to CLI calculator

choice = input("Which value would you like to perform the operation: if you want float then choose choice 1 if you want int then choose 2: ")
if choice == "1":
	num1 = float(input("Enter the value of float num1: "))
	num2 = float(input("Enter the value of float num2: "))

elif choice=="2":
	num1 = int(input("Enter the value of int num1: "))
	num2 = int(input("Enter the value of int num2: "))

else:

	print("Invalid choice")


print(" *********** choose operation to be performed *********** ")	


def add(num1,num2):
	return num1+num2

def sub(num1,num2):
	return num1-num2

def mul(num1,num2):
	return num1*num2

def div(num1,num2):
	return num1/num2

def mod(num1,num2):
	return num1%num2

def exp(num1,num2):
    return num1**num2


def input_value():
   if choice == "1":
   	num2 = float(input("Enter the value of int num2: "))
   	return num2
   elif choice=="2":
   	num2 = int(input("Enter the value of int num2: "))
   else:
   	print("Invalid choice!!")
   	




print("Choose the operator in which you want to perform opertaion:\n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4. Division \n 5.Modulus \n6.Exponential")
choice = input()
if choice=="1":
    a=add(num1,num2)
    print( num1, "+", num2 ,"=" , a)



elif choice=="2":
    b=sub(num1,num2)
    print( num1 ,"-", num2, "=" , b)



elif choice=="3":
    c=mul(num1,num2)
    print( num1 ,"*" ,num2 ,"=" , c)



elif choice=="4":
    if(num2==0):
    	num2=input_value()
    	f=div(num1,num2)
    	print( num1 ,"/", num2 ,"=" , f)
    else:
    	d=div(num1,num2)
    	print( num1 ,"/", num2 ,"=" , d)
       	


elif choice=="5":
    e=mod(num1,num2)
    print( num1 ,"%" ,num2 ,"=" , e)


elif choice=="6":   
    g=exp(num1,num2)
    print(num1,"**",num2,"=",g)


else:
    print("\nInvalid Operator!!")

	