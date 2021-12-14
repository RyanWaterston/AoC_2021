with open("/home/rwr/advent/day8/input.txt", "r") as input_file:
    lines = input_file.read().splitlines()

    total = 0
    for line in lines:
        signals, outputs = line.split(" | ")
        for o in outputs.split(" "):
            if len(o) in [2, 3, 4, 7]:
                total += 1

    print(f"Total: {total}")
