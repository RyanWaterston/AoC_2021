with open("/home/rwr/advent/day13/input.txt", "r") as input_file:
    lines = input_file.read()
    coords, folds = lines.split("\n\n")
    coords = [list(map(int, coord.split(","))) for coord in coords.split("\n")]
    folds = folds.split("\n")

    first_fold = [folds[0]]
    for fold in first_fold:
        fold_dir, fold_line = fold.split()[2].split("=")
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

    answer = list(set(map(tuple, coords)))
    print(f"Answer: {len(answer)}")
