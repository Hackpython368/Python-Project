def Timer():
    import time

    seconds = int(input("Enter the No of seconds : "))

    while True:
        time.sleep(1)
        seconds -= 1

        print(seconds)

        if seconds == 0 :
            print("Time over !")
            break


if __name__=="__main__":
    Timer()