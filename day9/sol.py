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

    lowest_points = []

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
            # print(f"{cave_map[row][col]} ", end="")
        # print()

    print(f"Lowest Points: {lowest_points}")
    print(f"Sum: {sum(lowest_points)}")
