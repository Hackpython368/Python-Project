import mysql.connector as mysql 

mysqlobject = mysql.connect(user='root',database='Birthday',host='Localhost',password='12345')

mycur = mysqlobject.cursor()


while True:
    name = input("Enter the name of the Birthday Boy/Girl : ")
    DOB = input("Enter the date of birth (YYYY-MM-DD) :")
    Wished = 0
    Number = input("Enter the no of the person :")

    mycur.execute("Insert into birthdate values('{}','{}',{},'{}')".format(name,DOB,Wished,Number))
    
    print("Do you want add more records ? (No - n / Yes - y) :")
    choice = input()

    if choice=='N' or choice =='n':
        print("Thank you !")
        mysqlobject.commit()
        break 
    
