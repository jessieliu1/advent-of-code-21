from util.util import file_to_caves
import sys
import copy

def path_count(filename):
    adj = file_to_caves(filename)
    # print(adj)
    seen = set()
    return find_paths("start", adj, seen)

def find_paths(cave, adj, seen):
    seen = copy.deepcopy(seen)

    # reached the end
    if cave == "end":
        return 1

    if cave.islower():
        seen.add(cave)

    # try the adjacent caves
    # print([find_paths(next_cave, adj, seen) for next_cave in adj[cave] if next_cave not in seen])
    return sum([find_paths(next_cave, adj, seen) for next_cave in adj[cave] if next_cave not in seen])

def path_count_pt2(filename):
    adj = file_to_caves(filename)
    seen = set()
    path = ""
    print(find_paths_pt2("start", adj, seen, False, path))
    return len(set(find_paths_pt2("start", adj, seen, False, path)))

# if the repeat is already used, add the cave to the seen set and no funny business
# if the repeat is not used, try both adding the cave to the seen set
# and repeat_used = false, and not adding the cave to the seen set and repeat_used = true
# if repeat not used, add other list of paths
def find_paths_pt2(cave, adj, seen, repeat_used, path: str):
    path += cave
    # reached the end
    if cave == "end":
        return [path] # list of strings

    seen = copy.deepcopy(seen)
    seen_ignore = copy.deepcopy(seen)

    if cave.islower():
        seen.add(cave)

    if cave == "start":
        seen_ignore.add(cave)

    cave_paths = []

    for next_cave in adj[cave]:
        if next_cave not in seen:
            if not repeat_used:
                cave_paths.extend(find_paths_pt2(next_cave, adj, seen_ignore, True, path))
            cave_paths.extend(find_paths_pt2(next_cave, adj, seen, repeat_used, path))
    return cave_paths

def main():
    print(path_count_pt2(sys.argv[1]))

main()
