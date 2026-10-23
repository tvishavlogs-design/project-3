print("=====ride builder=====")
print(" first pick one your vehicle")
print(" 1-bike")
print(" 2-car")
choice = int(input( "enter 1 or 2:"))
if choice == 1:
    print("now u need to pick which one")
    print("1-scooty")
    print("2- mountain bike")
bike_type=int(input("enter1 or2:"))
if bike_type==1:
    print("you picked scooty")
    print("speed-80kmph")
    print("best for 2 people")
if bike_type==2:
    print("you picked mountain bike")
    print("speed-100kmph")
    print("best for 2 people or races")
elif choice == 2:

    print("step 2: Pick your car type")
    print("( 1 - Sedan)")
    print("( 2 - SUV)")
    print()

    car_type = int(input("Enter 1 or 2: "))
    print()

    if car_type == 1:
        print("You picked  : Sedan")
        print("Seats       : 5 passengers")
        print("Best for    : Family trips")
    else:
        print("You picked  : SUV")
        print("Seats       : 7 passengers")
        print("Best for    : Off-road adventures")

else:
    print("That was not a valid choice.")
    print("Please enter 1 for Bike or 2 for Car.")
print("you are ready for a ride with your custom vehicle")
