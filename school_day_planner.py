print("--------- Smart school day planner -------------")
print("Answer three quick questions and I'll plan your day.")

day = input("Enter the day: ").strip().capitalize()
weather = input("Enter the weather (sunny/rainy/cloudy): ").strip().lower()
homework = input("Is your homework done? (y/n): ").strip().lower()

print()
print(f"=== YOUR PLAN FOR {day} ===")
print("-"*35)

if day in ("Saturday", "Sunday"):
    print("Day type: Weekend. Enjoy your free time!")
elif day == "Monday":
    print("The first day of the week. Pack you weekly planner.")
elif day == "Friday":
    print("The last school day. Return library books today.")
else:
    print("Day not recognised. Please check the spelling.")

if weather == "sunny" and homework == "y":
    print("Great weather and homework is done!")

if weather == "rainy" or weather == "cloudy":
    print("Pack your umbrella. It may get wet outside.")

if not (homework == "y"):
    print("Homework not done yet. Finish it before going out.")

if weather == "rainy" and not (homework == "y"):
    print("Stay in, finish homework then watch your favourite show.")
elif weather == "sunny" and homework == "y" and not (day in ("Saturday", "Sunday")):
    print("All set for a great school day. You're prepared.")
else:
    print("Best plan: take it one step at a time.")