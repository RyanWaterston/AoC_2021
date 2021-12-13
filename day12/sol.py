def follow_path(curr, dest, visited, path):
    if curr.islower():
        visited[curr] = True
    path.append(curr)

    if curr == dest:
        all_paths.append(path.copy())
    else:
        for i in _map[curr]:
            if visited[i] == False:
                follow_path(i, dest, visited, path)

    path.pop()
    visited[curr] = False


def get_paths(start, end):
    visited = {}
    for k in _map.keys():
        visited[k] = False

    path = []
    follow_path(start, end, visited, path)


with open("/home/rwr/advent/day12/input.txt", "r") as input_file:
    paths = [path.strip() for path in input_file.readlines()]
    all_paths = []
    _map = {}
    for path in paths:
        _from, _to = path.split("-")
        _map.setdefault(_from, []).append(_to)
        _map.setdefault(_to, []).append(_from)

    print(f"Mappings:")
    print(_map)

    get_paths("start", "end")

    print(f"Possible Paths: {len(all_paths)}")
