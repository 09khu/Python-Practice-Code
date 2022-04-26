num=int(input("enter a number: "))
if num>0:

    for i in range(2,num-1):
                   if(num%i==0):
                       print(num,"is not prime number")
                       break
    else:
        print(num,"is prime number")
                   
    
