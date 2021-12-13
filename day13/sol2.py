def print_paper(coords, num_of_rows, num_of_cols):
    print("Printing Paper:")
    print(coords)
    print(f"Row Size: {num_of_rows}    Col Size: {num_of_cols}")
    for r in range(num_of_rows):
        for c in range(num_of_cols):
            # print(f"Row: {r}  Col: {c}")
            found_coord = False
            for coord in coords:
                if c == coord[0] and r == coord[1] and not found_coord:
                    found_coord = True
                    # print([c, r])
                    print(f"#", end="")
            if not found_coord:
                print(f".", end="")
        print()
    print("==============")


with open("/home/rwr/advent/day13/input.txt", "r") as input_file:
    lines = input_file.read()
    coords, folds = lines.split("\n\n")
    coords = [list(map(int, coord.split(","))) for coord in coords.split("\n")]
    folds = folds.split("\n")

    num_of_cols = max([r[0] for r in coords]) + 1
    num_of_rows = max([r[1] for r in coords]) + 1
    for fold in folds:
        # print_paper(coords, num_of_rows, num_of_cols)
        fold_dir, fold_line = fold.split()[2].split("=")
        # print(f"Folding {fold_amount} in {fold_dir} direction")
        for idx, coord in enumerate(coords):
            x, y = coord
            if fold_dir == "y":  # fold bottom up
                if y > int(fold_line):
                    coords[idx][1] = 2 * int(fold_line) - y
            else:  # fold right to left
                if x > int(fold_line):
                    coords[idx][0] = 2 * int(fold_line) - x

        if fold_dir == "y":  # fold bottom up
            num_of_rows = int(fold_line)
        else:
            num_of_cols = int(fold_line)

    print_paper(coords, num_of_rows, num_of_cols)
