#import reduce module

from functools import reduce

list1=[2,13,42,4,524,331,452,321,22]
#list_even = list(filter(even,list1))#take two parametres 1.functions

#filter the even numbers from list

list_even =list(filter(lambda x:x%2==0,list1))
list_even =filter(lambda x:x%2==0,list1)
print(type(list_even))
list_odd = list(filter(lambda x:x%2!=0,list1))

print(list1)
print(list_even)
print(list_odd)

#using map function
list_even2 = list(map(lambda x:x*2,list_even))
print(list_even2)

#using reduce function to sum even numbers
sum=reduce(lambda x,y:x+y,list_even2)
print(sum)
