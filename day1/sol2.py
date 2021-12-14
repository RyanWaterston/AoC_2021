with open("/home/rwr/advent/day1/input2.txt") as input_file:
    lines = input_file.read().splitlines()
    increased = 0
    rolling_sum = int(lines[0]) + int(lines[1]) + int(lines[2])
    for idx in range(1, len(lines) - 2):
        next_sum = int(lines[idx]) + int(lines[idx + 1]) + int(lines[idx + 2])
        if next_sum > rolling_sum:
            increased += 1
        rolling_sum = next_sum
    print(f"# of times increased: {increased}")
