

file = open("input")
lines = file.readlines()
file.close()

max_calories = 0
current_calories = 0

for line in lines:
    data = line.strip()

    if len(data) == 0:
        if current_calories > max_calories:
            max_calories = current_calories
        current_calories = 0
    else:
        current_calories += int(data)

print(max_calories)

