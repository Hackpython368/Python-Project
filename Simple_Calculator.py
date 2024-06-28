def Calculator():
    Num1 = int(input("Enter the first Number :"))
    Num2 = int(input("Enter the second Number:"))
    Operation = input("Enter the Operation :")

    if Operation in ('-','+','/','*'):
        if Operation=='-':
            print("Calculating .....")
            print( Num1 - Num2)
        
        if Operation=='+':
            print("Calculating .....")
            print( Num1 + Num2)
        
        if Operation=='/':
            print("Calculating .....")
            print( Num1 / Num2)
        
        if Operation=='*':
            print("Calculating .....")
            print( Num1 * Num2)

    else :
        print("Invalid Operation !! ")


if __name__=="__main__":
    while True:
        print()
        print()
        print()
        print(" Welcome to the Calculator ")
        print()
        print()
        Calculator()
        print()
        print()
        print()
        option = input("Do you continue ? ('n','y') :")
        if option == 'n':
            print("Thank You !")
            break
        