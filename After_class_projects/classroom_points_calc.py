# Individual team points:
team1 = 43893
team2 = 8945
team3 = 84
team4 = 20
team5 = 3945

# Their total:
tot_points = team1 + team2 + team3 + team4 + team5
print("Together the classes earned", tot_points, "points.")

# Bonus for doing tasks on time and punishments for missing out on them:
bonus = 5
punishment = 10

tot_bonus = 8
tot_punishments = 10
print(
    "\nOver the week, the classes finished",
    tot_bonus,
    "tasks on time. However… they couldn't finish",
    tot_punishments,
    "tasks at all.",
)

bonus_points = bonus * tot_bonus
punishment_points = punishment * tot_punishments

# Actual total points and average points per class:
tot_points += bonus_points
tot_points -= punishment_points
average = tot_points / 5
print()
print("Now their total points are:", tot_points)
print("The average points per class are:", average)

# Number of reward stars earned:
stars_per_point = 3
tot_reward_stars = tot_points * stars_per_point
print("\nYour total reward stars are:", tot_reward_stars)

# Calculate the number of boxes you need to put in all the stars:
stars_per_box = 25
num_full_boxes = tot_reward_stars // stars_per_point
stars_left = tot_reward_stars % stars_per_box
print(num_full_boxes, "boxes will be filled.")
print(stars_left, "stars will be left.")

# Compare if you did better last week or this week:
last_week = 6032

print()
if last_week < tot_points:
    print("You reached more points than last week's points (" + str(last_week) + ")!")
elif last_week > tot_points:
    print("Oh no, your points have dropped compared to last week's points (" + str(last_week) + ")!")
else:
    print("You reached just as many points this week, as you did last week.")
