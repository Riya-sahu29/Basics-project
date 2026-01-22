# STONE PAPER AND  SCISSOR GAME
# We all have played stone, paper, scissor game in our childhood.If you haven't,google the rules of thos game and 
# write a python program capable of plyaing this game with the  user.

'''
1 for stone
-1 for paper
0 for scissor
'''
import random 
computer = random.choice([-1, 0, 1])
youstr = input("enter your choice: ")
youDict = {"st": 1, "p": -1, "s": 0}
reverseDict = {1: "stone", -1: "paper", 0: "scissor"}

you = youDict[youstr]

# By now we have 2 numbers (variables), you and computer 

print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer == you):
    print("its a draw")

else:
    if(computer ==-1 and you ==1):
        print("you lose!")

    elif(computer ==-1 and you ==0):
        print("you Win!")

    elif(computer ==1 and you ==-1):
        print("you Win!")

    elif(computer ==1 and you ==0):
        print("you lose!")

    elif(computer ==0 and you ==-1):
        print("you lose!")

    elif(computer ==0 and you ==1):
        print("you Win!")

    else:
        print("something went wrong!")


     