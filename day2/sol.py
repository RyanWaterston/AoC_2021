with open("/home/rwr/advent/day2/input.txt", "r") as input_file:
    lines = input_file.read().splitlines()
    init_pos = [0, 0]
    for line in lines:
        direction, distance = line.split(" ")
        distance = int(distance)
        if direction == "forward":
            init_pos[0] += distance
        if direction == "down":
            init_pos[1] += distance
        if direction == "up":
            init_pos[1] -= distance
    print(f"Final Position: {init_pos[0]}, {init_pos[1]}")
    print(f"Answer: {init_pos[0] * init_pos[1]}")
