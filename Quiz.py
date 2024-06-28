def feedback(marks):
    feedback = ['Excelent','Smart','Very Good','Good','Bad']

    if marks == 1:
        print(feedback[-1])
    if marks == 2:
        print(feedback[-2])
    if marks == 3:
        print(feedback[-3])
    if marks == 4:
        print(feedback[-4])
    if marks == 5:
        print(feedback[-5])



def Quiz():
    QuestionAndAnswer = [("Which device is used to hear music ?", "speaker"),("Full form  of CPU :","central processing unit"),("Which device is used to watch videos ?","moniter"),("Which device is used for typing the qustion in pc?","keyboard"),("Which device is used to take audio input ?","microphone")]

    print("Welcome to the Quiz Game ")

    marks = 0

    for i in QuestionAndAnswer:
        print()
        print(i[0])
        answer = input("").lower()

        if answer == i[1]:
            marks += 1
    
    feedback(marks)


if __name__=="__main__":
    Quiz()