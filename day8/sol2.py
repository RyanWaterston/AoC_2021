with open("/home/rwr/advent/day8/input.txt", "r") as input_file:
    lines = input_file.readlines()
    
    total = 0
    for line in lines:
        signals, outputs = line.strip().split(" | ")
        signals = sorted(signals.split(" "), key=len)
        print(signals)
        _map = {}
        _map[1] = signals[0]
        _map[4] = signals[2]
        _map[7] = signals[1]
        _map[8] = signals[-1]

        signals.remove(_map[1])
        signals.remove(_map[4])
        signals.remove(_map[7])
        signals.remove(_map[8])

        right = _map[1]
        mid_left = set(_map[4]) - set(_map[1])
        
        for s in signals:
            if len(s) == 6 and len(set(_map[4]) - set(s)) == 0:
                _map[9] = s
                signals.remove(s)
        for s in signals:
            if len(s) == 6 and len(set(s).intersection(mid_left)) == 1:
                _map[0] = s
                signals.remove(s)
        for s in signals:
            if len(s) == 6:
                _map[6] = s
        for s in signals:
            if len(s) == 5 and len(set(s).intersection(mid_left)) == 2:
                _map[5] = s
                signals.remove(s)
        for s in signals:
            if len(s) == 5 and len(set(s).intersection(right)) == 2:
                _map[3] = s
                signals.remove(s)
        _map[2] = signals[0]

        
        print(_map)

        for idx in range(len(_map)):
            _map[idx] = sorted(_map[idx])
    
        result = ""
        for o in outputs.split(" "):
            for idx in range(len(_map)):
                if sorted(o) == _map[idx]:
                    result += str(idx)
                    break
        print(f"{outputs} ", end="")
        print(result)
        print("--------------")
        total += int(result)
    print(total)
