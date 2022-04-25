
'''#x = "a+b-c/d"
x="22+18-19/110" 
print(x)
y=list(x)
print(y)'''

'''
x = "22+18/4-3"
print(x)
a=len(x)
print(a)'''
'''for i in range(len(x)):
    c =s[i];
    #if ((c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9')):'''

'''for i in range(len(x)):
    str_element  = x[i]
    if (str_element>='0' and str_element<='9'):
        operand = str_element'''

print("Program to convert an expression from infix to postfix: ")

def convert(exp):
    global top
    postfix=[]
    for i in exp:
        if(i.isdigit()):
            postfix.append(i)
        elif(i=="("):
            stk.append(i)
            top=top+1
            
        elif(i==")"):
            while(stk[top]!="("):
                postfix.append(stk.pop())
                top=top-1
            stk.pop()
            top=top-1
        else:
            if(top==-1):
                stk.append(i)
                top=top+1
            elif(stk[top]=='('):
                stk.append(i)
                top=top+1
            elif(priority(stk[top])>=priority(i)):
                postfix.append(stk.pop())
                top=top-1
                if(top>=0):
                    while(priority(stk[top]) == priority(i)):
                        postfix.append(stk.pop())
                        top=top-1
                        if(top<0):
                            break
                stk.append(i)
                top=top+1
            elif(priority(stk[top])<priority(i)):
                stk.append(i)
                top=top+1
                             
    while(top!=-1):
        postfix.append(stk.pop())
        top=top-1
    #print("The converted postfix string is: ",postfix)
    return postfix
    
def priority(op):
    if(op=='+' or op=='-'):
        return 1
    elif(op=='*' or op=='/'):
        return 2
    elif(op=='$'):
        return 3
    return 0



operator = ["+","-","/","*","%","(",")"]
numeral = ["0","1","2","3","4","5","6","7","8","9","."]
expression = []
a=input("int or float: ")
input_exp = input("Enter the expression : ")
print("Input =", input_exp)
operand = ""
top=-1
flag=0
for i in input_exp :
    if i in numeral :
        operand = operand+i
        flag=1
    elif i in operator :
        if(flag==1):
            expression.append(operand)
            operand = ""
            flag=0
            expression.append(i)
        else:
            expression.append(i)
    else :
        print("Invalid Character")
        break
if(flag==1):
    expression.append(operand)
print("Input (in list) = ", expression )
stk=[]
postfix=convert(expression)
print(postfix)



#Function to evaluate postfix expression: 


def postfix_evaluate(ev,a):
    flag=0
    for i in ev:
        if(i.isdigit()):
            stk.append(i)
        else:
            
            if(a=='int' and flag==0):
                op2=int(stk.pop())
                op1=int(stk.pop())
            else:
                op2=float(stk.pop())
                op1=float(stk.pop())
            if(i== '+'):
                stk.append(op1+op2)
            elif(i== '-'):
                stk.append(op1-op2)
            elif(i== '*'):
                stk.append(op1*op2)  
            elif(i== '/'):
                if(op1%op2!=0):
                    flag=1
                stk.append(op1/op2)
            elif(i== '^'):
                stk.append(pow(op1,op2))
    return stk.pop()


stk=[]



ans=postfix_evaluate(postfix,a)
print(ans)
        
        
