def check_adj(row, col):
    if (
        row < ROW_SIZE
        and col < COL_SIZE
        and row >= 0
        and col >= 0
        and flash_map[row][col] == 0
    ):
        energy_levels[row][col] += 1
        if energy_levels[row][col] > 9:
            flash(row, col)


def flash(row, col):
    if flash_map[row][col] == 1:
        return

    energy_levels[row][col] = 0
    flash_map[row][col] = 1

    up = row - 1
    down = row + 1
    left = col - 1
    right = col + 1

    check_adj(up, col)
    check_adj(down, col)
    check_adj(row, right)
    check_adj(row, left)

    check_adj(up, left)
    check_adj(up, right)
    check_adj(down, left)
    check_adj(down, right)


def print_map():
    for row in range(len(energy_levels)):
        for col in range(len(energy_levels[0])):
            print(f"{energy_levels[row][col]}", end="")
        print()
    print()


with open("/home/rwr/advent/day11/input.txt", "r") as input_file:
    lines = input_file.read().splitlines()
    energy_levels = [[int(o) for o in line] for line in lines]
    ROW_SIZE = len(energy_levels)
    COL_SIZE = len(energy_levels[0])

    flash_map = [[0 for i in range(COL_SIZE)] for j in range(ROW_SIZE)]
    flashes = 0

    print("Before steps:")
    print_map()

    for step in range(100):
        for row in range(ROW_SIZE):
            for col in range(COL_SIZE):
                energy_levels[row][col] += 1

        for row in range(ROW_SIZE):
            for col in range(COL_SIZE):
                if energy_levels[row][col] > 9:
                    flash(row, col)

        print(f"After {step+1} steps:")
        print_map()

        flashes += sum(map(sum, flash_map))
        flash_map = [[0 for i in range(COL_SIZE)] for j in range(ROW_SIZE)]

    print(f"Flashes: {flashes}")
