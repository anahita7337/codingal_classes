x = 5.5
if type(x) is int:
    print("true")
elif type(x) is float:
    print("true")
else:
    print("false")

print("Enter marks obtained in 5 subjects.")
mark1 = int(input())
mark2 = int(input())
mark3 = int(input())
mark4 = int(input())
mark5 = int(input())

total = mark1 + mark2 + mark3 + mark4 + mark5
average = int(total / 5)

valid_range = range(0, 101)

if average not in valid_range:
    print("Invalid input.")
elif average in range(91, 101):
    print("Your grade is A.")
elif average in range(70, 91):
    print("Your grade is B.")
else:
    print("Not A or B.")

# 6 = 0110
# 12 = 1100
# 5 and 3 = 0101 and 0011 = 0001 = 1
# 5 <<2 = 20
# 40 >>1 = 20
# 7 ^ 2 = 0111 ^ 0010 = 0101 = 5
# ~8 = -(8 + 1) = -9
