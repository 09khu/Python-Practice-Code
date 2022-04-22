#write a program to enter three test number and output best of two test numbers

first_test=float(input("Enter first test number :"))
second_test=float(input("Enter second test number :"))
third_test=float(input("Enter third test number :"))
if(third_test<first_test and third_test<second_test):
    result = first_test+second_test
elif(second_test<first_test and second_test<first_test):
    result = first_test+third_test
else:
    result = second_test+third_test
print("Best of two are :",result)