# ================================
# PERSONAL GOALS DISPLAY
# ================================

# ---------- PART 1: import the keyword module ----------
import keyword

# ---------- PART 2: ask the three questions ----------
# Ask for personal user values:
person_name = input("Enter your name: ")
goal_name = input("Enter one skill you want to get better at: ")
target_month = input("Enter the month you want to reach it by: ")

# ---------- PART 3: store the practice time ----------
# Daily minutes:
daily_minutes = 30

# ---------- PART 4: the heading ----------
# Heading for the display
print("\nMY PERSONAL GOAL PLAN\n")

# ---------- PART 5: the four plan lines ----------
# Four print() statements, each with a label and a variable separated by a comma:
print("Name:", person_name)
print("Goal:", goal_name)
print("Target month:", target_month)
print("Daily practice:", daily_minutes, "minutes")

# ---------- PART 6: two lines that join up ----------
# Show user status:
print("\nStatus:", "   ", end=" ")
print("Not started")

# Show user progress:
print("Reminder:", end=" - ")
print("Practise every day!")

# ---------- PART 7: the sentence and the keywords ----------
# One memorable sentence for the user to remember:
print("\nIn one sentence:")
print(
    person_name,
    "plans to work on",
    goal_name,
    "for",
    daily_minutes,
    "minutes every day until",
    target_month + ".",
)

# Python's reserved word list
print("\nWords python has reserved for itself:")
print(keyword.kwlist)
