

file = open("input")
lines = file.readlines()
file.close()

calories_list = list()
current_calories = 0

for line in lines:
    data = line.strip()

    if len(data) == 0:
        calories_list.append(current_calories)
        current_calories = 0
    else:
        current_calories += int(data)

calories_list.sort()

print(calories_list.pop() + calories_list.pop() + calories_list.pop())
