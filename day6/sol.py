DAYS = 80

with open("/home/rwr/advent/day6/input.txt", "r") as input_file:
    fish = input_file.readline().split(",")
    for idx, _ in enumerate(fish):
        fish[idx] = int(fish[idx])
    for day in range(DAYS):
        for idx, f in enumerate(fish):
            if f == 0:
                fish.append(9)
                fish[idx] = 6
            else:
                fish[idx] -= 1
        print(f"After {day+1} days: ", end="")
        #print(fish, end="")
        print(f"   =   {len(fish)}")
