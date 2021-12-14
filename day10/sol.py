with open("/home/rwr/advent/day10/input.txt", "r") as input_file:
    lines = input_file.read().splitlines()

    chunk_tags = {"(": ")", "[": "]", "{": "}", "<": ">"}
    score_map = {")": 3, "]": 57, "}": 1197, ">": 25137}

    wrong = []
    for line in lines:
        print(f"Processing Line: {line}")
        chunks_rem = []

        for c in line:
            if c in chunk_tags.keys():
                expected_chunk = chunk_tags[c]
                chunks_rem.append(expected_chunk)
            elif c in chunk_tags.values():
                next_tag = chunks_rem.pop()
                if c != next_tag:
                    print(f"Expected {next_tag} but found {c}")
                    wrong.append(c)
                    break

    total = 0
    for w in wrong:
        total += score_map[w]
    print(f"Total: {total}")
