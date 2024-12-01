ourMenu = {
    "Pizza" : 40, 
    "Coffee" : 30,
    "Pasta" : 50,
    "Burger" : 60,
    "Salad" : 30
}

for i in ourMenu:
     print(f"{i} : :  {ourMenu[i]} Rs")

count = 0
cost = 0


while True:
     if count==0:
         print("What do you want to order ?")
         order = input()
         cost += ourMenu[order]
         count += 1
     else:
          print("Do you want any thing elses ?")
          order = input()
          if order == "no" or order=="NO" or order == "No":
              print("Thank You For Visiting")
              print(f"Your Bill is ready of {cost} Rs.")
              break
          cost += ourMenu[order]    

     

    

