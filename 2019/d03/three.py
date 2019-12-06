def read_input():
    with open("2019/d03/three_input.txt") as f:
        return f.read().splitlines()


COMMANDS = {"R": (1, 0), "U": (0, 1), "L": (-1, 0), "D": (0, -1)}


def parse_wire(wire):
    for direction in wire.split(","):
        yield COMMANDS[direction[0]], int(direction[1:])


def generate_path(wire):
    path_x, path_y = 0, 0

    for (dx, dy), distance in parse_wire(wire):
        for _ in range(distance):
            path_x += dx
            path_y += dy

            yield path_x, path_y


def wire_intersections(wire_one, wire_two):
    return set(generate_path(wire_one)).intersection(generate_path(wire_two))


def manhattan_distance_for_paths(wire_one, wire_two):
    intersections = wire_intersections(wire_one, wire_two)
    return min(abs(x) + abs(y) for x, y in intersections)


# Part 2


def generate_path_and_steps(wire):
    path_x, path_y, steps = 0, 0, 0

    for (dx, dy), distance in parse_wire(wire):
        for _ in range(distance):
            path_x += dx
            path_y += dy
            steps += 1

            yield path_x, path_y, steps


def map_wires_paths_steps(wire_path):
    return {(path_x, path_y): step for path_x, path_y, step in wire_path}


def fewest_combined_steps(wire_one, wire_two):
    wire_one_path = generate_path_and_steps(wire_one)
    wire_two_path = generate_path_and_steps(wire_two)

    wire_one_paths_steps = map_wires_paths_steps(wire_one_path)
    wire_two_paths_steps = map_wires_paths_steps(wire_two_path)

    intersections = set(wire_one_paths_steps.keys()).intersection(
        wire_two_paths_steps.keys()
    )

    return min(
        wire_one_paths_steps[intersec] + wire_two_paths_steps[intersec]
        for intersec in intersections
    )


if __name__ == "__main__":
    print("Day 3 exercise...")

    wires = read_input()
    wire_one, wire_two = wires

    print(manhattan_distance_for_paths(wire_one, wire_two))

    print(fewest_combined_steps(wire_one, wire_two))
