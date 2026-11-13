temp = int(input("Enter today's temperature in Celcius: "))

if temp < 20:
    outfit = "Jacket"
    print("It is cold today.")
    print("Wear a", outfit)
else:
    outfit = "T-shirt"
    print("It is warm today.")
    print("Wear a", outfit)

is_raining = input("Is it raining today?(y/n): ")

if is_raining.lower().strip() == "y":
    print("Bring an umbrella.")
else:
    print("You don't need an umbrella.")
