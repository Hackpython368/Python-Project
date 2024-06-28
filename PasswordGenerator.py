def PasswordGenerator():
    SpecialCharater = "!@#$%^&*()_+~"
    Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = Alphabet.lower()
    Number =  "1234567890"

    length = int(input("Enter the length of the password : "))

    import random 

    choice = [SpecialCharater,Alphabet,alphabet,Number]
    password = ""

    while True:
        a = random.choice(choice)
        b = random.choice(a)

        password += b

        if len(password) == length :
            print(password)
            break

if __name__=="__main__":
    PasswordGenerator()