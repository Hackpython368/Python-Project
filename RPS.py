import random 

lst = ['Rock','Scissor','Paper']

def randomPicker(lst):
    return random.choice(lst)


while True :
    userInput = input("Enter the [Rock,Paper,Scissor] : ")
    compInput = randomPicker(lst)

    # print(compInput)

    if compInput=="Rock" :
        if userInput=="Paper":
            print("You Win!!")
        elif userInput=="Rock":
            print("Match Draw")
        else:
            print("Computer Win")
    if compInput=="Scissor":
        if userInput=="Rock":
            print("You Win!!")
        elif userInput=="Scissor":
            print("Match Draw")
        else:
            print("Computer Win")
    if compInput=="Paper":
        if userInput=="Scissor":
            print("You Win!!")
        elif userInput=="Paper":
            print("Match Draw")
        else:
            print("Computer Win")
