name = input("Enter your name: ")
age = int(input("Enter your age: "))
have_ticket = input("Do you have a ticket? (y/n): ")
weight = int(input("Enter the weight of your luggage: "))

if age < 18:
    print("You need an adult to travel with you.")
else:
    if have_ticket.lower().strip() == "y":
        pass
    else:
        pass
