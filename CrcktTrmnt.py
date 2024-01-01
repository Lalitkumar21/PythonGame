import sys
import time as t

a=input("Please Enter your name:")
t.sleep(1)
print("Hii",a,"Welcome to the Cricket Tournament")
t.sleep(1)
print("It's an International Tournament game in Cricket's World")
print("-"*20)
t.sleep(1)
print("Now, You have to select Your country")
t.sleep(1)
print("Available countries are:")
x=["India,Pakistan,Australia,SouthAfrica,SriLanka,WestIndies"]
t.sleep(1)
print(x)
t.sleep(1)
print("""
            for India : Enter 1,
            for Pakistan : Enter 2,
            for SouthAfrica : Enter 3,
            for SriLanka : Enter 4,
            for WestIndies : Enter 5,\n""")

def country():

    t.sleep(2)
    b=int(input("Enter Number for your selected country:"))
    if (b==1):
        print("You have selected India")
        t.sleep(1)
    elif (b==2):
        print("You have selected Pakistan")
        t.sleep(1)
    elif (b==3):
        print("You have selected SouthAfrica")
        t.sleep(1)
    elif (b==4):
        print("You have selected SriLanka")
        t.sleep(1)
    elif (b==5):
        print("You have selected WestIndies")
        t.sleep(1)
    else:
        print("Please Enter valid number!!!")
        country()
country()
#Against Team
print("And your Against team is Bangladesh\n")

#Toss
print("Now It,s Time to TOSS")
t.sleep(1)
print("""
         For Head: Press H
         For Tail: Press T\n""")
def HT():
    c=input("Choose Head Or Tail:")
    if c=="H":
        t.sleep(1)
        print("""
            Opposite Team Win toss
                   AND
            They Choose bowling First.""")
    elif c=="T":
        t.sleep(1)
        print("""
            Opposite Team Win toss
                   AND
            They Choose bowLing First.""")
    elif c=="h":
        t.sleep(1)
        print("""
            Opposite Team Win toss
                   AND
            They Choose bowling First.""")
    elif c=="t":
        t.sleep(1)
        print("""
            Opposite Team Win toss
                   AND
            They Choose bowling First.""")
    else:
        t.sleep(1)
        print("Select Valid")
        print(HT())
HT()
t.sleep(1)
print("\nNow Your team is on Batting\n")
print("-"*20)

#For Batsmen
t.sleep(1)
print("#Batsmen#")
t.sleep(1)
print("Now It,s Time to choose Your Batsmen")
t.sleep(1)
print("Select from below")
t.sleep(1)
print("For Virender Sehwag : Enter VS")
t.sleep(1)
print("For Sachin Tendulkar : ST")
t.sleep(1)
print("For Virat Kohli : VK")
t.sleep(1)
print("""         OR        """)
t.sleep(1)
print("Enter any Random Player as your own")
t.sleep(1)
p=input("Enter your player as your opening Batsmen:")

if p=="VS" or p=="vs":
    print("You Selcted Virender Sehwag as your opening Batsmen")
elif p=="ST" or p=="st":
    print("You Selcted Sachin Tendulkar as your opening Batsmen")
elif p=="VK" or p=="vk":
    print("You Selcted Virat Kohli as your opening Batsmen")
else:
    print("You Selcted",p," as your opening Batsmen")

#NOTES
t.sleep(1)   
print("\nMatch is of 1 over i.e. 6 Balls")
t.sleep(1)
print("Bangladesh choose Mustafizur Rahman for Bowling")

#GAME STARTED
t.sleep(1)
print("Get Ready For Your Game")
t.sleep(1)
print(""" \n                      "GAME STARTED"             \n""")
t.sleep(1)
print("So Now you are on pitch")
t.sleep(1)
print("""\nBefore we start NOTE Following:
                    HIT (Type)    ENTER
                    FOR Straight :S
                    FOR Left     :L
                    FOR Back     :B
                    For Defend   :D\n""")
t.sleep(3)
print("Mustafizur Rahman throw the ball towards you.")
t.sleep(1)          
a=["Swing","Bounce","Straight","Spin",]
RUN=[4,6,0]
import random as r
arr=[]

b=r.choice(a)
 
print("The ball is looking like",b)  

def hit():
    S="Straight"
    L="Left"
    B="Back"
    D="Defend"
    c=r.choice(RUN)
    t.sleep(1)
    print("You have 3 sec to Enter Type of Hit")
    start_time=t.time()
    HIT=input("Enter type of HIT you want to use(fast): ")
    end_time=t.time()
    while True:
        time_taken=end_time-start_time
        if time_taken<=5:
            if HIT=="S" or HIT=="s":
                print("YOU Hit",S)
                print("You Scored:",c)
                arr.append(c)
                break
            elif HIT=="L" or HIT=="l":
                print("YOU Hit",L)
                print("You Scored:",c)
                arr.append(c)
                break
            elif HIT=="B" or HIT=="b":
                print("YOU Hit",B)
                print("You Scored:",c)
                arr.append(c)
                break
            elif HIT=="D" or HIT=="d":
                print("YOU Hit",D)
                c=0
                print("You scored",c)
                arr.append(c)
                break
        else:
            ("Clean Bold!!! Time up!!!")
            sys.exit()

def Totlscore():
    sum=0
    for i in range(6):
        sum=sum+arr[i]
    print(sum)
        
for i in range(0,6):
    hit()
    print()
    if i==5:
        break
    t.sleep(1)
    print("Now It's Time to Move on!!")
    t.sleep(1)
    print("Bowler is going to throw Second ball")

Totlscore()
print(arr)
