#Print table of user defined number


a = int(input("Enter a number"))
#num = 0
print(a)
b=a*10
count=0

for i in range(a,b+1,a):
    count=count+1
    '''print(a, "*" ,num, " = " ,i)'''
    print("{} * {} = {}".format(a,count,i))