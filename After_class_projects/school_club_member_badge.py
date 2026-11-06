# ================================
# SCHOOL CLUB MEMBER BADGE
# ================================

# ---------- PART 1: member details ----------
# Get the club's and member's name:
member = input("Enter the member's name: ")
club = input("Enter the club's name: ")

# ---------- PART 2: data types ----------
# Hardcode values
mem_num = 8
points = 9.5
is_active = True

print("\nThe type of the number of total members is: ", type(mem_num))
print("The type of the total points is: ", type(points))
print("The status of whether they are active is: ", type(is_active))

# ---------- PART 3: badge code ----------
# Create the badge code by combining the first three letters of the member's name, 
# the last letter of the club and the number of total members:

mem_num = str(mem_num)
points = str(points)
is_active = str(is_active)

badge_code = member[0:3] + club[-1] + mem_num
print("\nThe code of their badge is:", badge_code)

# ---------- PART 4: final badge ----------
# Concluding lines on the existing info:
print("\n===== CLUB BADGE =====")
print("The member is called: " + member)
print("The club is called: " + club)
print("The code is: " + badge_code)
print("The total points are: " + points)
print("Is the member active: " + is_active)
