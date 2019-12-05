def read_input():
    with open("2019/d03/three_input.txt") as f:
        return f.read().splitlines()


COMMANDS = {'R': (1, 0), 'U': (0, 1), 'L': (-1, 0), 'D': (0, -1)}
def generate_path(wire):
    path_x, path_y = 0, 0

    for direction in wire.split(","):
        dx, dy = COMMANDS[direction[0]]
        distance = int(direction[1:])

        for _ in range(distance):
            path_x += dx; path_y += dy

            yield path_x, path_y


def wire_intersections(wire_one, wire_two):
    return set(generate_path(wire_one)).intersection(generate_path(wire_two))


def manhattan_distance_for_paths(wire_one, wire_two):
    intersections = wire_intersections(wire_one, wire_two)
    return min(abs(x) + abs(y) for x, y in intersections)


if __name__ == "__main__":
    print("Day 3 exercise...")

    wires = read_input()
    wire_one, wire_two = wires

    print(manhattan_distance_for_paths(wire_one, wire_two))
