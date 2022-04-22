#To find greater number among three numbers by taking values by users.

a,b,c=int(input("Enter first number\n")),int(input("Enter second number\n")),int(input("Enter third number\n"))

#b=int(input("Enter second number\n"))
#c=int(input("Enter third number\n"))

'''if(a==b==c):
    print("All values are equal")
elif(a>b)and(a>c):
    print(a,"is greater than",b ,"and",c)
elif(b>c) and (b>a):
    print(b,"is greater than",a,"and",c)
else:
    print(c,"is greater than",b,"and",a)'''
    
if(a==b==c):
    print("All values are equal")
elif(a==b)and (a>c):
    print("a and b are equal and is  greater than c")
elif(a==b)and (a<c):
    print("a and b are equal and is  less than c")    
elif(b==c) and (b>a):
    print("b and c are equal and  is greater than a")
elif(b==c) and (b<a):
    print("b and c are equal and  is less than a")    
elif(c==a)and(c>b):
    print("a and c are equal and greater than b")
elif(a>b)and(a>c):
    print(a,"is greater than",b,"and",c)
elif(b>c) and (b>a):
    print(b,"is greater than",a,"and",c)
else:
    print(c,"is greater than",b,"and",a)
