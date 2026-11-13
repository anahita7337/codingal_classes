# ----------------------------------------
# DAILY ACTIVITY PLANNER
# ----------------------------------------

# Ask the user how much time they need to complete their homework:
time = int(input("Enter the time you need to do your homework in minutes: "))

# Check if the homework takes long or not and pick an appropriate plan:
if time > 60:
    plan = "Start your homework now."
    print("That's quite a long homework session.")
else:
    plan = "Finish your homework quickly."
    print("That's a pretty short homework session.")

# Check if user will have any freetime at all and if so remind them to pick a hobby:
any_freetime = input("Is there any free time after your homework? (yes/no): ")
any_freetime = any_freetime.lower().strip()

# Precaution: Just in case the user types in something like pizza or simply presses enter:
if any_freetime != "yes":
    any_freetime = "no"

if any_freetime == "yes":
    print("REMINDER: Pick a hobby for you free time!")

# Print the overview of the whole plan that the user can follow daily:
print("\n====== DAILY PLAN ======")
print("Minutes for homework:", time)
print("Plan:", plan)
print("Free time:", any_freetime)

