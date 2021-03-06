def read_input():
    with open("2019/d02/two_input.txt") as f:
        return list(map(int, f.read().replace("\n", "").split(",")))


def pre_process(program):
    program[1] = 12
    program[2] = 2

    return program


def process_opcode(opcode, element_one, element_two):
    if opcode == 1:
        return element_one + element_two

    if opcode == 2:
        return element_one * element_two

    raise StopIteration()


def chunks(lst):
    for i in range(0, len(lst), 4):
        chunk = lst[i : i + 4]

        if len(chunk) == 4:
            yield chunk


def process_program(program):
    try:
        for chunk in chunks(program):
            opcode = chunk[0]
            element_one_pos = chunk[1]
            element_two_pos = chunk[2]
            output_pos = chunk[3]

            element_one = program[element_one_pos]
            element_two = program[element_two_pos]

            program[output_pos] = process_opcode(opcode, element_one, element_two)
    except StopIteration:
        pass

    return program


def possible_inputs():
    return [(x, y) for x in range(100) for y in range(100)]


def process_program_two(program):
    for first_elem, second_elem in possible_inputs():
        new_program = list(program)

        new_program[1] = first_elem
        new_program[2] = second_elem

        final = process_program(new_program)

        if final[0] == 19690720:
            return first_elem, second_elem


if __name__ == "__main__":
    print("Day 2 exercise...")

    input_content = read_input()
    program = pre_process(input_content)

    processed_program = process_program(list(program))

    print(f"Part 1: {processed_program[0]}")

    processed_program = process_program_two(list(program))

    print(f"Part 2: {100 * processed_program[0] + processed_program[1]}")
