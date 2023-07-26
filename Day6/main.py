import os

with open(os.path.dirname(__file__) + "\\input.txt", "r") as file:
    input = file.read()
for i in range(3, len(input)):
    l = set(list(input[i-3:i+1]))
    if (len(l) == 4):
        break
first_package_marker = i + 1
print(f"First start-of-package marker after character {first_package_marker}.")
for i in range(13, len(input)):
    l = set(list(input[i-13:i+1]))
    if (len(l) == 14):
        break
first_message_marker = i + 1
print(f"First start-of-message marker after character {first_message_marker}.")