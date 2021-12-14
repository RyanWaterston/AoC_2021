SIZE = 1000
vent_map = [[0 for j in range(SIZE)] for i in range(SIZE)]


with open("/home/rwr/advent/day5/input.txt", "r") as input_file:
    lines = input_file.read().splitlines()
    for line in lines:
        coords = line.split(" ")
        x1, y1 = coords[0].split(",")
        x2, y2 = coords[2].split(",")
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)

        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for y in range(y1, y2 + 1):
                vent_map[x1][y] += 1
        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            for x in range(x1, x2 + 1):
                vent_map[x][y1] += 1
        else:
            # diagonal
            vent_map[x1][y1] += 1
            while x1 != x2 and y1 != y2:
                if x1 < x2:
                    x1 += 1
                else:
                    x1 -= 1
                if y1 < y2:
                    y1 += 1
                else:
                    y1 -= 1
                vent_map[x1][y1] += 1

    danger = 0
    for y in range(SIZE):
        for x in range(SIZE):
            if vent_map[x][y] >= 2:
                danger += 1

    print(f"Dangerous Areas: {danger}")
