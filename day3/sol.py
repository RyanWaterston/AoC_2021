BITS = 12

with open("/home/rwr/advent/day3/input.txt", "r") as input_file:
    lines = input_file.read().splitlines()
    one_bits = [0 for i in range(BITS)]
    gamma_bits = ["0" for i in range(BITS)]
    epsilon_bits = ["1" for i in range(BITS)]
    for line in lines:
        for i in range(BITS):
            one_bits[i] += int(line[i])

    for i in range(BITS):
        if one_bits[i] >= len(lines) / 2:
            gamma_bits[i] = "1"
            epsilon_bits[i] = "0"

    gamma_bits = "".join(gamma_bits)
    epsilon_bits = "".join(epsilon_bits)

    e_bits = int(gamma_bits, 2)
    print(f"Epsilon Bits: {e_bits}")
    e_bits = ~int(gamma_bits, 2) & 0xFFF
    print(f"Epsilon Bits: {e_bits}")

    print(f"Gamma Bits: {gamma_bits}")
    print(f"Gamma Decimal: {int(gamma_bits, 2)}")
    print(f"Epsilon Bits: {epsilon_bits}")
    print(f"Epsilon Decimal: {int(epsilon_bits, 2)}")
    print(f"Multiplied together: {int(gamma_bits, 2) * int(epsilon_bits, 2)}")
