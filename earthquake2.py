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

category = 1 if magnitude < 2.0 else 2 if magnitude < 4.0 else 3 if magnitude < 5.0 else 4 if magnitude < 6.0 else 5 if magnitude < 7.0 else 6 if magnitude < 8.0 else 7

match category:
    case 1:
        print("Micro")
        print("No danger")
    case 2:
        print("Minor")
        print("Prepare for an emergency")
    case 3:
        print("Light")
        print("Stay indoors")
    case 4:
        print("Moderate")
        print("Stay indoors")
    case 5:
        print("Strong")
        print("Evacuate quickly")
    case 6:
        print("Major")
        print("Evacuate immediately")
    case 7:
        print("Great")
        print("Evacuate now")
