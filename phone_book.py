class contact:
	def __init__(self,fname,lname,phone_no):
		self.fname=fname
		self.lname=lname
		self.phone_no=phone_no

	def getdata(self):
	    f=open("phonebook.text","w")
	    

	def putdata(self):
		global phonebook
		
		phonebook=open("phonebook.text","w")
		phonebook.write(fname)
		phonebook.write("\n")
		phonebook.write(lname)
		phonebook.write("\n")
		phonebook.write(phone_no)
		phonebook.close()

fname=input("Enter first name: ")
lname=input("Enter last name: ")
phone_no=input("Enter number: ")

c1=contact(fname,lname,phone_no)
u1=c1.putdata()

#fname lname address email contact1 cpntact2 category 


