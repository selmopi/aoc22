
file = open("input")
lines = file.readlines()
file.close()

map1 = {"A": 1, "B": 2, "C": 3 }
map2 = {"X": 1, "Y": 2, "Z": 3 }
points = 0

for line in lines:
    a = line[0]
    b = line[2]

    a_value = map1.get(a)
    b_value = map2.get(b)

    points += b_value

    if a_value == b_value: # draw
        points += 3
    elif (b_value == 1 and a_value == 3) or \
            (b_value == 2 and a_value == 1) or \
            (b_value == 3 and a_value == 2) :# you won
        points += 6
    # else you lose

print(points)
