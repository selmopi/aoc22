    
def elena(char):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return 1 + alphabet.find(char)


def josef(char):
    value = 0

    if char >= 'A' and char <= 'Z':
        value = 27 + ord(char) - ord('A')
    elif char >= 'a' and char <= 'z':
        value = 1 + ord(char) - ord('a')
    
    return value


def main():
    file = open("input")
    lines = file.readlines()
    file.close()

    n = 0
    for line in lines:
        line = line.strip()
        length = len(line)
        rucksack_size = length / 2
    
        first_half = line[0:int(rucksack_size)]
        second_half = line[int(rucksack_size):]

        for char in first_half:
            if second_half.find(char) > -1:
                n += josef(char)
                break

    print(n)

if __name__ == "__main__":
    main()
