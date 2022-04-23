'''i=1
while(i<10):
    print(i)
    i=i+1 '''


year = int(input("Enter a numebr: "))

if(year % 400  ==0)and (year % 100==0):
    
    print("leap year")
elif(year%4==0)and (year%100!=0):
    print("leap year")
else:
    print("not a leap year")




