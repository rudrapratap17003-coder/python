print("SMART ROOM CONTROL SYSTEM")
while True:
    # Get room status from smartphone
    room = input("\nIs the room occupied? (yes/no): ")

    # If room is occupied
    if room == "yes":

        # Get temperature
        temperature = float(input("Enter room temperature: "))

        print("\nRoom is occupied.")
        print("Temperature:", temperature, "°C")

        # Temperature condition
        if temperature < 20:
            print("AC: OFF")
            print("Fan: OFF")
            print("Reason: Temperature is below 20°C.")

        elif temperature >= 20:
            print("AC: ON")
            print("Fan: OFF")
            print("Reason: Temperature is 20°C or above.")

    # If room is empty
    elif room == "no":

        print("\nRoom is empty.")
        print("AC: OFF")
        print("Fan: OFF")

    # Invalid input
    else:
        print("Invalid input! Please enter yes or no.")

    # Continue or stop
    choice = input("\nDo you want to check again? (yes/no): ")

    if choice == "no":
        print("\nSmart Room System Closed.")
        break