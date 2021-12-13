def follow_path(curr, dest, _counts, path):
    _counts[curr] -= 1
    path.append(curr)

    if curr == dest:
        all_paths.append(path.copy())
    else:
        for i in _map[curr]:
            if _counts[curr] >= 0 and i != "start":
                follow_path(i, dest, _counts, path)

    path.pop()
    _counts[curr] += 1


def get_paths(start, end):
    _counts = {}
    for k in _map.keys():
        if k.islower() and k not in ["start", "end"]:
            _counts[k] = 1
        else:
            _counts[k] = 100

    for k in _map.keys():
        if k.islower() and k not in ["start", "end"]:
            # allow each small cave to be visited twice
            _counts[k] = 2
            path = []
            follow_path(start, end, _counts, path)
            _counts[k] = 1


with open("/home/rwr/advent/day12/input.txt", "r") as input_file:
    paths = [path.strip() for path in input_file.readlines()]
    all_paths = []
    _map = {}
    _counts = {}
    for path in paths:
        _from, _to = path.split("-")
        _map.setdefault(_from, []).append(_to)
        _map.setdefault(_to, []).append(_from)

    for k in _map.keys():
        if k.islower() and k not in ["start", "end"]:
            _counts[k] = 1
        else:
            _counts[k] = -1

    print(f"Mappings:")
    print(_map)

    get_paths("start", "end")

    print(f"Paths: ")
    all_paths = set(map(tuple, all_paths))
    all_paths = map(list, all_paths)
    all_paths = sorted(all_paths)
    # for p in all_paths:
    #    print(p)
    print(f"Possible Paths: {len(all_paths)}")
