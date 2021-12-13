with open("/home/rwr/advent/day10/input.txt", "r") as input_file:
    lines = input_file.readlines()

    chunk_tags = {
        '(' : ')',
        '[' : ']',
        '{' : '}',
        '<' : '>'
    }
    score_map = {
        ')' : 1,
        ']' : 2,
        '}' : 3,
        '>' : 4
    }

    wrong = []
    incomplete = []
    for line in lines:
        line = line.strip()
        incomplete.append(line)
        #print(f"Processing Line: {line}")
        chunks_rem = []

        for c in line:
            if c in chunk_tags.keys():
                expected_chunk = chunk_tags[c]
                chunks_rem.append(expected_chunk)
            elif c in chunk_tags.values():
                next_tag = chunks_rem.pop()
                if c != next_tag:
                    #print(f"\nExpected {next_tag} but found {c}")
                    wrong.append(c)
                    incomplete.remove(line)
                    break

    totals = []
    for line in incomplete:
        print(f"Processing Line: {line}")
        chunks_rem = []

        for c in line:
            if c in chunk_tags.keys():
                expected_chunk = chunk_tags[c]
                chunks_rem.append(expected_chunk)
            elif c in chunk_tags.values():
                chunks_rem.pop()

        chunks_rem.reverse()
        print(f"Complete by adding {''.join(chunks_rem)}")

        total = 0
        for c in chunks_rem:
            total = (total * 5) + score_map[c]
        print(f"Total: {total}")
        totals.append(total)

    print(f"Answer: {sorted(totals)[len(totals) // 2]}")
