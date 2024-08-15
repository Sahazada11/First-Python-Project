import random


computer=random.choice([-1,1,0])
user=input("Enter Your Choice: ")
gameDict={"stone":1,"paper":-1,"sezer":0}
userdict=gameDict[user]
reversedict={1:'stone',-1:'paper',0:'sezer'}
print(f'You Choice {reversedict[userdict]}\nComputer Choice {reversedict[computer]}')
print("")

if (computer==userdict):
    print("Draw\nTry Again")
    print("")
else:
    if(computer==1 and userdict==-1):
        print("You Win!,Congratulation")
        print("")
    elif(computer==1 and userdict==0):
        print("You Lose!,Better Luck Next Time")
        print("")
    elif(computer==-1 and userdict==1):
        print("You Lose!,Better Luck Next Time")
        print("")
    elif(computer==-1 and userdict==0):
        print("You Win!,Congratulation")
        print("")
    elif(computer==0 and userdict==1):
        print("You Win!,Congratulation")
        print("")
    elif(computer==-0 and userdict==-1):
        print("You Lose!,Better Luck Next Time")
        print("")
    else:
        print("Somthing Went Wrong!, Please Try Again")
        print("")
    