DAYS = 256
FISH = [0 for i in range(9)]


with open("/home/rwr/advent/day6/input.txt", "r") as input_file:
    fish = input_file.readline().split(",")
    for idx, _ in enumerate(fish):
        FISH[int(fish[idx])] += 1
    
    for day in range(DAYS):
        old_fish = FISH[0]
        new_fish = FISH[8]

        for i in range(8):
            FISH[i] = FISH[i+1]

        FISH[6] += old_fish
        FISH[8] = old_fish

    count = 0
    for f in FISH:
        count += f
        
    print(f"After {DAYS} days: {count}")
