# Student App Access Manager
# Permission values stored as binary bits:
CAMERA = 1  # 0001
MICROPHONE = 2  # 0010
STORAGE = 4  # 0100

# App lists:
approved_apps = ["coding app", "math app", "reading app", "science app"]
restricted_apps = ["gaming app", "shopping app", "social media app"]

# Get the requested app:
requested_app = input("Enter the app you want to access: ").lower()


print("\n--- Identity Operator Check ---")
student_age = 11
if type(student_age) is int:
    print("The student age is stored as a number.")
if type(student_age) is not str:
    print("The student age is not stored as text.")


print("\n--- Membership Operator Check ---")
if requested_app in approved_apps:
    print(f"{requested_app} is an approved student app.")
else:
    print(f"{requested_app} is not an approved student app.")

if requested_app not in restricted_apps:
    print("The app is not in the restricted list.")
else:
    print("Access denied because the app is restricted.")


print("\n--- App Permission Settings ---")
student_permissions = CAMERA | MICROPHONE

print("Permission bits:", bin(student_permissions))
if student_permissions & CAMERA is not 0:
    print("Camera permission: Enabled")
if student_permissions & MICROPHONE is not 0:
    print("Microphone permission: Enabled")
if STORAGE is 0:
    print("Storage permission: Enabled")
else:
    print("Storage permission: Disabled")

print("\n--- Bit Shift Demonstration ---")
print("Camera bit:", bin(CAMERA))
print("After left shift:" and bin(CAMERA << 1))
print("Storage bit:", bin(STORAGE))
print("After right shift:" and bin(STORAGE >> 1))

print("\n--- Final Access Result ---")
if (requested_app in approved_apps) & (requested_app not in restricted_apps):
    print(f"Access granted to {requested_app}")
else:
    print(f"Access denied to {requested_app}")
