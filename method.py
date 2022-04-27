'''
method
class methiod
static methon
instance method :- which work on an instance'''
class student():
    institution="IIPS" #belomgs to class

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def show(self):
        print("-------------------------------")
        print("Marks in python = ",self.a)
        print("Marks in python lab = ",self.b)
        
        print("-------------------------------")
        
    @classmethod
    def info(self):
        print("class belongs to",self.institution)
    @staticmethod
    def about():
        print("This class holds the data of marks obtained by students in python and its lab in IIPS")

s1 = student(12,10)

s2 = student(13,11)

s3 = student(14,9)

s1.show()
s2.show()
s3.show()
student.info()
student.about()
#print(student.institute)
