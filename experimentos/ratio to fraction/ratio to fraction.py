from time import sleep
from file import simplify
while True:

    numerator = input("input a ratio:  _:y  -  ")
    if numerator.lower() != "stop":
        try:
            int(numerator)
        except:
            print("the text you typed is not a number.")
            continue

    elif numerator.lower() == "stop":
        print("ok! tata bye bye!")
        break

    else:
        print("somthing went wrong...")
        sleep(2)
        print("crashing prograram...")
        sleep(2)
        break

    denominator = input(f"                {numerator}:_  -  ")
    if denominator.lower() != "stop":
        try:
            int()
        except:
            print("the text you typed is not a number.")
            continue

    elif denominator.lower() == "stop":
        print("ok! tata bye bye!")
        break

    else:
        print("somthing went wrong...")
        sleep(2)
        print("crashing prograram...")
        sleep(2)
        break

    numerator = int(numerator)
    denominator = int(denominator)
    print(f"{numerator}:{denominator}")
    simplified = simplify(numerator, denominator)
    print(f"{numerator}:{denominator}  =  {simplified[0]}/{simplified[1]}")
