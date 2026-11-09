field1 = 120
field2 = 85
field3 = 150
field4 = 95
field5 = 110

tot = field1 + field2 + field3 + field4 + field5
tot += 30
# tot = tot + 30
average = tot / 5
average1 = tot // 5

print(tot, "; ", average)
print(average1)

num = float(input("Enter a number: "))

if num % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")


number = float(input("Enter a number: "))
if number > 20:
    print("Greater than 20.")
elif number < 20:
    print("Smaller that 20.")
else:
    print("Equal to 20.")

num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
num3 = float(input("Enter a number: "))

if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)

password = input("Enter your password: ")

if password == "Anahita":
    print("Access granted.")
else:
    print("Access declined.")

value = float(input("Enter a number: "))

if value % 3 != 0:
    print("Your number is not divisible by three.")
else:
    print("Your number is divisible by three.")
