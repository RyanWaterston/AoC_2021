with open("/home/rwr/advent/day1/input.txt") as input_file:
    lines = input_file.readlines()
    increased = 0
    for idx, line in enumerate(lines[1:]):
        if int(line) > int(lines[idx]):
            increased += 1
    print(f"# of times increased: {increased}")
