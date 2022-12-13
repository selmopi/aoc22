
import copy

def to_grid(lines):
    grid = list()

    for line in lines:
        line = line.strip()

        x = list()
        grid.append(x)
        for char in line:
            x.append(int(char))

    return grid


def main():
    file = open("input")
    lines = file.readlines()
    file.close()

    forest = to_grid(lines)
    forest_h = len(forest)
    forest_l = len(forest[0])

    visible = set()

    # Add visible trees for each row.
    for y in range(forest_h):
        tallest = None
        max_height = 0

        # Get first tallest from left.
        for x in range(forest_l):
            height = forest[y][x]

            if height > max_height:
                tallest = (x, y)
                max_height = height
                visible.add(tallest)
          
        # Get first tallest from right.
        max_height = 0
        for x in range(forest_l - 1, -1, -1):
            height = forest[y][x]

            if height > max_height:
                tallest = (x, y)
                max_height = height
                visible.add(tallest)
    
    # Add visible trees for each column.
    for x in range(forest_l):
        tallest = None
        max_height = 0

        # Get first tallest from top.
        for y in range(forest_h):
            height = forest[y][x]

            if height > max_height:
                tallest = (x, y)
                max_height = height
                visible.add(tallest)
          
        # Get first tallest from right.
        max_height = 0
        for y in range(forest_h - 1, -1, -1):
            height = forest[y][x]

            if height > max_height:
                tallest = (x, y)
                max_height = height
                visible.add(tallest)
    

    # Add trees on the border.
    for y in range(forest_h):
        visible.add((0, y))
        visible.add((forest_l - 1, y))
 
    for x in range(forest_l):
        visible.add((x, 0))
        visible.add((x, forest_h - 1))
     

    print(len(visible))


if __name__ == "__main__":
    main()
