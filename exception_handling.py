try:
	a = int(input("Enter a Integer : "))
	b = int(input("Enter a Integer (except 0) : "))
	c = a / b
	print(a, '/', b, '=', c)
except ZeroDivisionError:
	print("Can't Divide by 0")
except ValueError :
	print("Please Enter a Valid Integer Value")
finally:
	print("BYE !")