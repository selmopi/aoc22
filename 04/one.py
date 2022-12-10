
# Check whether the interval (a, b) is contained in
# the interval (x, y).
#
def is_contained(a, b):
    a_bottom = int(a[0])
    a_top = int(a[1])
    b_bottom = int(b[0])
    b_top = int(b[1])
    return (a_bottom >= b_bottom and a_top <= b_top)

def main():
    file = open("input")
    lines = file.readlines()
    file.close()
    
    n = 0
    
    for line in lines:
        line = line.strip()
        
        pair = line.split(",")
    
        first_section = pair[0].split("-")
        second_section = pair[1].split("-")
        
        if (is_contained(first_section, second_section) or is_contained(second_section, first_section)):
            n +=1

    print(n)


if __name__ == "__main__":
    main()
