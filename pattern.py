'''for i in range(1,5,1):
    n="*"*i
    print(n)


print("This script is intended to swap the values of two data variable using a third temporary variable")
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
print("Before swapping")
print("a = ",a)
print("b = ",b)
temp=a
a=b
b=temp
print("After swapping")
print("a = ",a)
print("b = ",b)
print("Values after swapping : ")
print("a = "+str(a))
print("b = "+str(b))'''

print("This script is intended to swap the values of two data variable using a third temporary variable")
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
print("Before swapping")
print("a = ",a)
print("b = ",b)
'''a=a+b
b=a-b
a=a-b
print("After swapping")
print("a = ",a)
print("b = ",b)'''

a,b=b,a
print("After swapping")
print("a = ",a)
print("b = ",b)

