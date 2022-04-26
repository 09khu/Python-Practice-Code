# Rock paper scissor game

print("Enter 1 for rock\nEnter 2 for paper\nEnter 3 for scissor")

p1=int(input("Player 1 \n Enter Your Choice : "))
p2=int(input("Player 2 \n Enter Your Choice : "))

if(p1<1 or p1>3):
    print("Player 1 please enter a valid Number!!!")
elif(p2<1 or p2>3):
    print("Player 2 please enter a valid Number!!!")
elif(p1==p2):
    print("Match Draw!!!!!!!!!")
elif(p1==1 and p2==2):
    print("Player 2(Paper) has Won!!!!!!!!!")
elif(p1==1 and p2==3):
    print("Player 1(Rock) has Won!!!!!!!!!")
elif(p1==2 and p2==1):
    print("Player 1(Paper) has Won!!!!!!!!!")
elif(p1==2 and p2==3):
    print("Player 2(Scissor) has Won!!!!!!!!!")
elif(p1==3 and p2==1):
    print("Player 2(Rock) has Won!!!!!!!!!")
elif(p1==3 and p2==2):
    print("Player 1(Scissor) has Won!!!!!!!!!") 
