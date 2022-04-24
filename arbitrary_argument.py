#Program of arbirary argument

def avg(* value):
    x=0
    for i in value:
        x=x+i
    return x/len(value)

y=avg(3,4,5,12,34)
print(y)