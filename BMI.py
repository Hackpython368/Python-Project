def CalculateBMI():
    height = float(input("Enter your height in meter  :"))
    weight = int(input("Enter your weight in KG :"))

    print(f"Body Mass Index is {int(weight/(height*height))}")

if __name__=="__main__":
    CalculateBMI()