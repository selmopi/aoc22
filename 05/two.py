
def main():
    file = open("input")

    # List of stacks.
    stacks = dict()

    # Get the stack map.
    while line := file.readline() :
        line = line.strip()
        
        # Break when finding empty line.
        if len(line) == 0:
            break;

        # Parse stack map.
        for i in range(1, len(line), 4):
            id = str(line[i]).strip()
            
            if len(id) != 0:
                n = int(((i - 1) / 4) + 1)
                stack = stacks.get(n)
                if stack is None:
                    stack = list()
                    stacks[n] = stack
                stack.append(id)

    # Fix stacks order.
    for stack in stacks.values():
        stack.reverse()

    # Get and apply the rearrengement procedure.
    while line := file.readline() :
        line = line.strip()

        words = line.split(" ")
        n = words[1]
        from_n = words[3]
        to_n = words[5]
        temp_stack = list()

        for i in range(int(n)):
            from_stack = stacks.get(int(from_n))
            temp_stack.append(from_stack.pop())

        for i in range(int(n)):
            to_stack = stacks.get(int(to_n))
            to_stack.append(temp_stack.pop())

    file.close()

    # Get results.
    results = ""
    stack_size = 10
    for i in range(1, int(stack_size)):
        results += str(stacks.get(i).pop())
    print(results)

if __name__ == "__main__":
    main()
