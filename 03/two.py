    
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

    n = 0
    while first := file.readline().strip() :
        second = file.readline().strip()
        third = file.readline().strip()

        for char in first:
            if second.find(char) > -1 and third.find(char) > -1:
                n += elena(char)
                break

    file.close()

    print(n)

if __name__ == "__main__":
    main()
