
import copy

def see(height, vector):
    n = 0
    for h in vector:
        n += 1
        if h >= height:
            break

    return n


def get_scenic_score(a, b, forest):
    forest_l = len(forest[0])
    forest_h = len(forest)
    height = forest[b][a]

    top = list()
    x = a
    for y in range(b - 1, -1, -1):
        top.append(forest[y][x])
    top_score = see(height, top)

    bottom = list()
    for y in range(b + 1, forest_h):
        bottom.append(forest[y][x])
    bottom_score = see(height, bottom)

    left = list()
    y = b
    for x in range(a - 1, -1, -1):
        left.append(forest[y][x])
    left_score = see(height, left)

    right = list()
    for x in range(a + 1, forest_l):
        right.append(forest[y][x])
    right_score = see(height, right)

    return top_score * bottom_score * left_score * right_score
    


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

    max_scenic_score = 0

    for y in range(forest_h):
        for x in range(forest_l):
            scenic_score = get_scenic_score(x, y, forest)

            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

    print(max_scenic_score)


if __name__ == "__main__":
    main()
