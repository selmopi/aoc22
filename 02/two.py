
file = open("input")
lines = file.readlines()
file.close()

map1 = {"A": 1, "B": 2, "C": 3 }
map2 = {"X": 0, "Y": 3, "Z": 6 }
points = 0

for line in lines:
    a = line[0]
    b = line[2]

    a_value = map1.get(a)
    b_value = map2.get(b)

    # add outcome points
    points += b_value

    # Add shape poins 
    if b_value == 3: # draw
        points += a_value # you choose the same as your opponent
    elif b_value == 6: # win
        if a_value == 1:
            points += 2
        elif a_value == 2:
            points += 3
        else:
            points += 1
    else: # lose
        if a_value == 1:
            points += 3
        elif a_value == 2:
            points += 1
        else:
            points += 2


print(points)
