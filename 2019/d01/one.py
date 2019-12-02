def read_input():
    with open("2019/d01/one_input.txt") as f:
        return list(map(int, f))


def fuel_requirement(mass):
    return mass // 3 - 2


def _fuel_requirement_fuel(fuel):
    while True:
        fuel = fuel_requirement(fuel)

        if fuel <= 0:
            break

        yield fuel


def fuel_requirement_fuel(fuel):
    return sum(_fuel_requirement_fuel(fuel))


if __name__ == "__main__":
    modules = read_input()

    print(modules)

    part_one = sum(fuel_requirement(module) for module in modules)
    print(f"Part 1: {part_one}")

    part_two = sum(fuel_requirement_fuel(module) for module in modules)
    print(f"Part 2: {part_two}")
