BITS = 12


def get_rate(values, _type="oxygen"):
    for i in range(BITS):
        one_list = [line for line in values if line[i] == "1"]
        zero_list = list(set(values) - set(one_list))

        if (_type == "oxygen" and len(one_list) >= len(values) / 2) or (
            _type == "co2" and len(one_list) < len(values) / 2
        ):
            values = one_list
        else:
            values = zero_list

        if len(values) == 1:
            return values


with open("/home/rwr/advent/day3/input.txt", "r") as input_file:
    lines = input_file.read().splitlines()

    oxy = get_rate(lines, _type="oxygen")
    co2 = get_rate(lines, _type="co2")

    print(oxy)
    print(co2)
    print(int(str(oxy[0]), 2) * int(str(co2[0]), 2))
