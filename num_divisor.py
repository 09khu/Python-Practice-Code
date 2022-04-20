# Program that asks the user for a number and then prints out a list of all the divisors of that number. 


num = int(input("Enter number to print its divisor: "))
print("All divisor of",num,"is: ")
for i in range(1,num+1):
    if num%i==0:
       print(i)
       i=i+1
