import os

print("=" * 8, "SWIMMING POOL ENTRY CHECKER", "=" * 8)
# Ask for age:
age = int(input("Enter your age: "))

# Age group recognition:
if age <= 0:
    print("Time traveler detected!")
    os._exit(1)
elif age < 4:
    age_group = "toddler"
elif age < 13:
    age_group = "kid"
elif age < 18:
    age_group = "teenager"
elif age < 60:
    age_group = "adult"
elif age >= 60 and age <= 100:
    age_group = "senior"
else:
    print("You are too old to learn swimming!")
    os._exit(1)

# Check if they can swim and if an adult is nearby:
can_swim = input("Can you swim? (y/n): ").strip().lower()
adult_here = input("Is there an adult nearby? (y/n): ").strip().lower()

# Suggest a suitable pool for the swimmer:
if age_group == ("toddler" or "kid"):
    pool = "Shallow end"
elif can_swim == "y" and adult_here == "y":
    pool = "Deep pool"
else:
    pool = "Shallow end"

# Print the final info:
print("-" * 50)
print("The final decision:")
print(f"Age group: {age_group}")
print(f"Pool: {pool}")

# Remind the swimmer to get a lifeguard in case of emergency:
if not (adult_here == "y"):
    print("Remember to get a lifeguard!")

print("\nHave a nice swim!\n")
