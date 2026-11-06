name = input("Enter your real name: ")
gadget = input("Enter your favourite gadget: ")

agent_number = 7
speed_rating = 9.5
height = 1.65
is_active = True

print()
print("The real name is", name, "Type of name is: ", type(name))
print("The gadget is", gadget, "Type of gadget is: ", type(gadget))
print("The agent number is", agent_number, "Type of agent number is: ", type(agent_number))
print("The speed rating is", speed_rating, "Type of speed rating is: ", type(speed_rating))
print("The height is", height, "Type of height is: ", type(height))
print("Is active:", is_active, "Type of is active is: ", type(is_active))

print()
agent_number = str(agent_number)
height = str(height)
print(agent_number, type(agent_number))
print(height, type(height))

print()
print(name[3:5])
name1 = "Anahita"
name1 = name1[::-1]
print(name1)