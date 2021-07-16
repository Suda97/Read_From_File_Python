def names():
    f = open("names.txt", "r")
    print(f.read())
    f.close()


def pictures():
    counter = {}
    with open('pictures.txt') as f:
        line = f.readline()
        while line:
            line = line[3:-26]
            if line in counter:
                counter[line] += 1
            else:
                counter[line] = 1
            line = f.readline()

    print(counter)


if __name__ == '__main__':
    print("1. Names\n2. Pictures")
    u = input("Choose option (1-2): ")
    if u == "1":
        names()
    elif u == "2":
        pictures()
    else:
        print("WRONG INPUT!")
