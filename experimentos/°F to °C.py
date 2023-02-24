from time import sleep
while True:

    farhaneite_value = input("°F: ")
    if farhaneite_value.lower() != "stop":
        try:
            float(farhaneite_value)
        except:
            print("the text you typed is not a number.")
            continue

    elif farhaneite_value.lower() == "stop":
        print("ok! tata bye bye!")
        break

    else:
        print("somthing went wrong...")
        sleep(2)
        print("crashing prograram...")
        sleep(2)
        break

    farhaneite_value = float(farhaneite_value)
    print(f"°C: {(farhaneite_value - 32) * 5/9}")
