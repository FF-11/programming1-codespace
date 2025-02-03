while True:
    try:
        magnitude: float = float(input("magnitude (double) "))
    except ValueError:
        print("Invalid input. Try again.")
    else:
        if magnitude < 0.0:
            print("Negative numbers are not allowed.")
        else:
            break
if magnitude < 2.0:
    print("Micro")
    print("No danger")
elif magnitude < 4.0:
    print("Minor")
    print("Prepare for an emergency")
elif magnitude < 5.0:
    print("Light")
    print("Stay indoors")
elif magnitude < 6.0:
    print("Moderate")
    print("Stay indoors")
elif magnitude < 7.0:
    print("Strong")
    print("Evacuate quickly")
elif magnitude < 8.0:
    print("Major")
    print("Evacuate immediately")
else:
    print("Great")
    print("Evacuate now")
