
# Parse input.
# Assume current working directory as root.
# Returns a list of directories, tuples containing name and size.
#
def parse_input(lines_iterator):
    dirs = dict()
    dir_name = "/"
    dir_size = 0

    try:
        while line := next(lines_iterator):
            line = line.strip()

            words = line.split(" ")
            if words[0] == "$":  # command
                if words[1] == "cd":  # change directory
                    if words[2] == "..":
                        break

                    # Get dir name.
                    subdir_name = words[2]

                    # Recursive call to get dir size, and subdirs info.
                    subdirs = parse_input(lines_iterator)

                    # Prepend subdir names with current working directory.
                    # Directory names become paths. And add them to dirs.
                    for subdir in subdirs.items():
                        new_subdir_name = "/" + subdir_name + subdir[0]
                        dirs[new_subdir_name] = subdir[1]

                    # Add size of the outermost subdirectory to the current
                    # working directory size.
                    dir_size += subdirs.get("/")

                elif words[1] == "ls":
                    pass

            else:  # listing
                if words[0].isnumeric():
                    dir_size += int(words[0])
                else:
                    pass

    except Exception as e:
        pass

    dirs[dir_name] = dir_size
    return dirs

def main():
    # Get input.
    file = open("input")
    lines = file.readlines()
    file.close()

    lines_iterator = iter(lines)
    # Skip first 'cd /'
    next(lines_iterator)
    dirs = parse_input(lines_iterator)

    n = 0
    for dir in dirs.items():
        if int(dir[1]) <= 100000:
            n += dir[1]
    
    print(n)


if __name__ == "__main__":
    main()

