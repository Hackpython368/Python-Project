def TempConvert():
    temp = int(input("Enter Temperature in Celsius :"))

    Fahrenheit = (temp * 5/9) + 32 

    print()
    print(f"Temperature in  Fahrenheit is {Fahrenheit} F")

def DistanceConvert():
    Miles = int(input('Enter the distance in Miles : '))

    KM = Miles * 1.60

    print()
    print(f"The distance in KiloMeter is {KM}")

def WeightConvert():
    Pounds = int(input("Enter the weight in Pounds :"))

    KG = Pounds / 2.20

    print()
    print(f"The weight in KiloGram is {KG}")



def main():
    while True:
        print("Welcome to the unit converter ")

        print()
        print("1. Convert Celsius to Fehranheit ")
        print("2. Convert Miles to KiloMeter ")
        print("3. Convert Pounds to KoliGram ")
        print("4. Exit ")

        Choice = int(input("Enter your choice :"))
        if Choice == 1: 
            TempConvert()
        elif Choice == 2:
            DistanceConvert()
        elif Choice == 3:
            WeightConvert()
        elif Choice == 4:
            break
        else:
            print("Wrong Input !!!")


if __name__=="__main__":
    main()