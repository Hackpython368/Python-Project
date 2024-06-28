def Game():
    print("This is a Number Gussing . Where you have to Guss a  no between 1 - 100 .")

    import random 

    random_number = random.randint(1,101)

    while True:
        print("Enter your Guss :")
        guss = int(input())
        if guss == random_number:
            print("Conguration , You got the number . ")
            break

        if guss > random_number:
            print("Greater")

        if guss < random_number:
            print("Low")

if __name__=="__main__":
    print()
    print("STARTING THE GAME")
    print()
    Game()