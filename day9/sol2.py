def check_location(row, col):
    basins = 1

    if row < 0 or row >= ROW_SIZE or col < 0 or col >= COL_SIZE:
        return 0

    if int(cave_map[row][col]) == 9 or checked_map[row][col] == 1:
        return 0

    checked_map[row][col] = 1

    basins += check_location(row - 1, col)
    basins += check_location(row + 1, col)
    basins += check_location(row, col - 1)
    basins += check_location(row, col + 1)

    return basins


with open("/home/rwr/advent/day9/input.txt", "r") as input_file:
    lines = input_file.read().splitlines()

    cave_map = []
    for line in lines:
        row = []
        for height in line:
            row.append(height)
        cave_map.append(row)

    ROW_SIZE = len(cave_map)
    COL_SIZE = len(cave_map[0])

    checked_map = [[0 for j in range(COL_SIZE)] for i in range(ROW_SIZE)]

    lowest_points = []
    locations = []

    for row in range(ROW_SIZE):
        for col in range(COL_SIZE):
            is_lowest = True

            height = cave_map[row][col]
            up = row - 1
            down = row + 1
            left = col - 1
            right = col + 1

            if left >= 0:
                is_lowest = is_lowest and height < cave_map[row][left]
            if right < COL_SIZE:
                is_lowest = is_lowest and height < cave_map[row][right]
            if up >= 0:
                is_lowest = is_lowest and height < cave_map[up][col]
            if down < ROW_SIZE:
                is_lowest = is_lowest and height < cave_map[down][col]

            if is_lowest:
                lowest_points.append(int(height) + 1)
                locations.append((row, col))
            # print(f"{cave_map[row][col]} ", end="")
        # print()

    print(f"Lowest Points: {lowest_points}")
    print(f"Locations: {locations}")

    basins = []
    for location in locations:
        row = location[0]
        col = location[1]

        basin = check_location(row, col)
        basins.append(basin)

    top_basins = sorted(basins)[-3:]
    print(f"Answer: {top_basins[0]*top_basins[1]*top_basins[2]}")
