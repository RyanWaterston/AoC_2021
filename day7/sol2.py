with open("/home/rwr/advent/day7/input.txt", "r") as input_file:
    line = input_file.readline()
    positions = sorted(map(int, line.split(",")))

    fuel_used = 0
    best_alignment = 10000000000
    for align in range(positions[0], positions[-1]):
        fuel_used = 0
        for p in positions:
            fuel_used += sum(range(abs(p - align)+1))
            #print(f"{p} used {sum(range(abs(p-align)))}")
        if fuel_used < best_alignment:
            best_alignment = fuel_used

    print(f"Best Alignment: {best_alignment}")
