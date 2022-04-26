#************ for w
f = open("My first file.text" ,"w")
x = "Hello, Good morning"
y = " Have a nice day!!"
f.write(x)
f.write("\n")
f.write(y)
f.close()


#************* for reading operation***************
f = open("My first file.text" ,"r")
x = f.read()
print(x)
f.close()
